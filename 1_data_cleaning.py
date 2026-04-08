import pandas as pd

# 1. Load the data
df = pd.read_excel('Walmart.xlsx')

# 2. Fix the Dates (Very important for Time Series!)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.sort_values('Order Date')

# 3. Create 'Elite' Features (The stuff that makes you stand out)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Week_of_Year'] = df['Order Date'].dt.isocalendar().week

# 4. Group by Date to see total daily sales
# Retailers care about total volume per day/week
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()

print("Data Cleaned! Here is the head:")
print(daily_sales.head())

# Save this cleaned version for the next step
daily_sales.to_csv('cleaned_sales.csv', index=False)