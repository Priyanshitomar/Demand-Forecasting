import pandas as pd
from src.utils.config import FORECAST_OUTPUT


def load_forecast():
    return pd.read_csv(FORECAST_OUTPUT)


def suggest_inventory(predicted_sales, safety_factor=1.2):
    return round(predicted_sales * safety_factor, 2)


def generate_inventory_report():
    df = load_forecast().tail(7)

    print("\n📦 INVENTORY REPORT")
    print("-" * 40)

    for _, row in df.iterrows():
        stock = suggest_inventory(row['yhat'])
        print(f"{row['ds']} | Predicted: {round(row['yhat'],2)} | Stock: {stock}")

    print("-" * 40)