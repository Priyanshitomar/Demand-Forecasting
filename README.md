 🚀 Walmart Demand Forecasting & Inventory Optimization

The Business Problem
Retailers lose millions due to inventory imbalances. This project automates demand forecasting to reduce overstock costs and prevent lost sales from understocking.

🛠️ Technical Architecture
* **Data Pipeline:** Automated cleaning and feature engineering using **Pandas**.
* **Forecasting Engine:** Leveraged **Meta's Prophet** model to capture complex seasonality and holiday impacts.
* **Business Intelligence:** Built an interactive **Streamlit** dashboard to visualize forecasts and stock requirements.

📈 Key Insights & Results
* **Model Performance:** Achieved an **MAE of 255.93** and **RMSE of 522.03** on test data.
* **Weekly Trends:** Identified significant sales spikes on weekends, allowing for targeted labor and supply scheduling.
* **Inventory Optimization:** Implemented a **1.2x Safety Stock** logic to provide a 20% buffer against demand volatility.

**💻 How to Run**
1.  **Run Pipeline:** `python main.py` to process data and generate forecasts.
2.  **Launch Dashboard:** `streamlit run streamlit_app.py` to view interactive reports.
