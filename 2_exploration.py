import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_sales.csv', parse_dates=['Order Date'])

plt.figure(figsize=(12,6))
sns.lineplot(x='Order Date', y='Sales', data=df)
plt.title('Walmart Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()