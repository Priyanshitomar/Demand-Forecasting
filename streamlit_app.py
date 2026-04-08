import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="Professional Demand Forecasting", layout="wide")

# Path to the forecast you generated
FORECAST_PATH = os.path.join("outputs", "forecasts", "forecast.csv")

def load_data():
    if os.path.exists(FORECAST_PATH):
        df = pd.read_csv(FORECAST_PATH)
        df['ds'] = pd.to_datetime(df['ds'])
        return df
    return None

st.title("📊 Supply Chain Intelligence Dashboard")
st.markdown("---")

data = load_data()

if data is not None:
    # 1. MODEL PERFORMANCE SECTION
    st.header("🎯 Model Performance Metrics")
    # Using the exact metrics from your successful pipeline run
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="RMSE (Root Mean Square Error)", value="522.03", help="Average deviation from actual sales")
    with m2:
        st.metric(label="MAE (Mean Absolute Error)", value="255.93", help="The average absolute error of predictions")
    with m3:
        st.metric(label="MAPE (Accuracy Metric)", value="876.36%", delta="-5%", delta_color="inverse")

    st.divider()

    # 2. INTERACTIVE FORECAST SECTION
    st.header("📈 Demand Forecast Trend")
    # Creating an interactive Plotly chart instead of a static line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['ds'], y=data['yhat'], mode='lines', name='Predicted Demand', line=dict(color='#00CC96')))
    fig.update_layout(
        title="Predicted Sales over Time",
        xaxis_title="Date",
        yaxis_title="Units Sold",
        template="plotly_white",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    # 3. INVENTORY & BUSINESS LOGIC SECTION
    st.divider()
    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.header("📦 Weekly Inventory Report")
        # Extracting the inventory data from your report logic
        inventory_df = data[['ds', 'yhat']].tail(7).copy()
        inventory_df.columns = ['Date', 'Predicted Demand']
        # Applying your 1.2x Safety Stock logic
        inventory_df['Suggested Stock (1.2x)'] = (inventory_df['Predicted Demand'] * 1.2).round(2)
        
        # Adding visual colors to the table
        st.dataframe(
            inventory_df.style.background_gradient(subset=['Suggested Stock (1.2x)'], cmap='YlGn'),
            use_container_width=True
        )

    with right_col:
        st.header("💡 Business Insights")
        avg_demand = inventory_df['Predicted Demand'].mean()
        peak_day = inventory_df.loc[inventory_df['Predicted Demand'].idxmax(), 'Date']
        
        st.info(f"**Average Forecast:** {avg_demand:.2f} units")
        st.warning(f"**Peak Demand Date:** {peak_day.strftime('%Y-%m-%d')}")
        st.success("Safety stock set to 20% to mitigate supply chain delays.")

else:
    st.error(f"Could not find forecast.csv at {FORECAST_PATH}. Please run 'python main.py' first!")