import pandas as pd
from src.preprocessing.clean_data import run_cleaning
from src.preprocessing.feature_engineering import run_feature_engineering

from src.models.baseline import train_baseline
from src.models.ml_models import train_random_forest
from src.models.prophet_model import train_prophet, evaluate_prophet, forecast

from src.evaluation.metrics import evaluate_model
from src.business.inventory_logic import generate_inventory_report

def run_pipeline():
    print("🚀 Starting pipeline...\n")

    run_cleaning()
    run_feature_engineering()

    results = []

    print("📈 Training Prophet model...")
    p_model, p_df = train_prophet()
    p_y_true, p_y_pred = evaluate_prophet(p_model, p_df)
    results.append(evaluate_model(p_y_true, p_y_pred, "Prophet"))
    forecast(p_model, p_df)

    print("\n📊 MODEL COMPARISON")
    print("-" * 50)

    for r in results:
        print(f"{r['Model']}")
        print(f"RMSE: {r['RMSE']:.2f}")
        print(f"MAE: {r['MAE']:.2f}")
        print(f"MAPE: {r['MAPE']:.2f}%")
        print("-" * 50)

    generate_inventory_report()

    print("\n✅ Pipeline completed.")