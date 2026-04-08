import os

import pandas as pd
from src.utils.config import DATA_PATH, PROCESSED_PATH


def load_data():
    return pd.read_excel(DATA_PATH)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df = df.sort_values('Order Date')
    df = df.dropna()
    return df

def save_data(df: pd.DataFrame):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)


def run_cleaning():
    df = load_data()
    df = clean_data(df)
    save_data(df)
    print("✅ Data cleaned and saved.")
