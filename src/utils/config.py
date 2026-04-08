import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "walmart.xlsx")
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_data.csv")

FORECAST_OUTPUT = os.path.join(BASE_DIR, "outputs", "forecasts", "forecast.csv")