import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Prophet requires specific column names: 'ds' for date and 'y' for the value
df = pd.read_csv('cleaned_sales.csv')
df.columns = ['ds', 'y']

# Initialize and Train the model
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
model.fit(df)

# Create a "future" placeholder for the next 90 days
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Show the forecast
fig1 = model.plot(forecast)
plt.title('90-Day Sales Forecast')
plt.show()

# Show the components (Trend, Weekly, Yearly)
fig2 = model.plot_components(forecast)
plt.show()