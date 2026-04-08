import pandas as pd

# 1. Load the forecast we created in the last step
# (Note: In a real project, we'd save the forecast to CSV, but let's use the 'forecast' variable if you are in a notebook, or re-run the logic)
# For this script, let's assume we are transforming the forecast into 'Orders'

def suggest_inventory(predicted_sales, safety_factor=1.2):
    """
    Business Logic: We don't just stock exactly what we predict. 
    We stock a bit more (Safety Stock) to ensure we don't run out if the model is slightly off.
    """
    return round(predicted_sales * safety_factor, 2)

# Let's simulate a 'Manager Report' for the next 7 days
# (In your real project, you would pull these from the 'forecast' dataframe)

print("--- WALMART INVENTORY REPLENISHMENT REPORT ---")
print("Date       | Predicted Sales | Recommended Stock to Order")
print("-" * 55)

# Example sample data derived from your model's output
sample_dates = ['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04', '2014-01-05']
predictions = [1250.50, 1100.20, 1450.75, 2100.00, 1850.30]

for date, pred in zip(sample_dates, predictions):
    stock_needed = suggest_inventory(pred)
    print(f"{date} | ${pred:<14} | ${stock_needed}")

print("-" * 55)
print("STRATEGY: Using a 20% Safety Stock buffer to prevent stock-outs during volatility.")