import pandas as pd
from src.utils.config import PROCESSED_PATH


def load_data():
    return pd.read_csv(PROCESSED_PATH, parse_dates=['Order Date'])

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Week'] = df['Order Date'].dt.isocalendar().week.astype(int)
    return df


def create_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Lag_1'] = df['Sales'].shift(1)
    df['Lag_2'] = df['Sales'].shift(2)
    df['Rolling_Mean_4'] = df['Sales'].rolling(4).mean()
    return df


def run_feature_engineering():
    df = load_data()
    df = create_time_features(df)
    df = create_lag_features(df)

    df = df.dropna()
    df.to_csv(PROCESSED_PATH, index=False)

    print("✅ Features created and saved.")