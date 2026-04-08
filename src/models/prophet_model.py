import pandas as pd
from prophet import Prophet
from src.utils.config import PROCESSED_PATH, FORECAST_OUTPUT


def prepare_data():
    df = pd.read_csv(PROCESSED_PATH)
    df = df.rename(columns={
        'Order Date': 'ds',
        'Sales': 'y'
    })
    return df


def train_prophet():
    df = prepare_data()

    model = Prophet()

    # Add external regressors
    regressors = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

    for reg in regressors:
        if reg in df.columns:
            model.add_regressor(reg)

    model.fit(df)

    print("✅ Prophet model trained.")
    return model, df


def forecast(model, df):
    future = model.make_future_dataframe(periods=30)

    # Fill regressors forward (simple strategy)
    for col in ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']:
        if col in df.columns:
            future[col] = df[col].iloc[-1]

    forecast = model.predict(future)

    import os
    os.makedirs(os.path.dirname(FORECAST_OUTPUT), exist_ok=True)
    forecast[['ds', 'yhat']].to_csv(FORECAST_OUTPUT, index=False)

    print("✅ Forecast saved.")
    return forecast

def evaluate_prophet(model, df):
    forecast = model.predict(df)

    y_true = df['y']
    y_pred = forecast['yhat']

    return y_true, y_pred