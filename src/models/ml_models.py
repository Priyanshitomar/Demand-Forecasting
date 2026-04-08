import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from src.utils.config import PROCESSED_PATH


def load_data():
    df = pd.read_csv(PROCESSED_PATH)
    return df


def prepare_data(df):
    features = ['Lag_1', 'Lag_2', 'Rolling_Mean_4']
    target = 'Weekly_Sales'

    X = df[features]
    y = df[target]

    return train_test_split(X, y, shuffle=False)


def train_random_forest():
    df = load_data()
    X_train, X_test, y_train, y_test = prepare_data(df)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test