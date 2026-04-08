import reflex as rx
import pandas as pd
import os

# Updated path to reach back out to your project's data folder
# This assumes the CSV is at: Demand Forecasting/outputs/forecasts/forecast.csv
DATA_PATH = os.path.join(os.getcwd(), "..", "outputs", "forecasts", "forecast.csv")

class State(rx.State):
    df: pd.DataFrame = pd.DataFrame()
    # Data for the chart
    chart_data: list[dict] = []
    metrics: dict = {"RMSE": "522.03", "MAE": "255.93", "MAPE": "876.36%"}

    def load_data(self):
        if os.path.exists(DATA_PATH):
            full_df = pd.read_csv(DATA_PATH)
            # Take the latest 15 days for the chart
            recent_df = full_df.tail(15)
            self.df = recent_df.head(10)
            # Format data for Reflex Recharts
            self.chart_data = recent_df.apply(
                lambda row: {"name": row["ds"], "value": round(row["yhat"], 2)}, 
                axis=1
            ).to_list()
        else:
            print(f"File not found at: {DATA_PATH}")

def stats_card(label, value):
    return rx.vstack(
        rx.text(label, font_size="0.8em", color="gray"),
        rx.text(value, font_size="1.5em", font_weight="bold"),
        padding="1em",
        border="1px solid #e1e4e8",
        border_radius="10px",
        width="100%",
    )

def index():
    return rx.container(
        rx.vstack(
            rx.heading("Demand Forecasting Dashboard", size="8", margin_bottom="0.5em"),
            
            # Metrics Row
            rx.hbox(
                stats_card("RMSE", State.metrics["RMSE"]),
                stats_card("MAE", State.metrics["MAE"]),
                stats_card("MAPE", State.metrics["MAPE"]),
                width="100%",
                spacing="4",
            ),

            rx.divider(margin_y="2em"),

            # Forecast Graph
            rx.heading("Demand Forecast Trend", size="5"),
            rx.recharts.area_chart(
                rx.recharts.area(
                    data_key="value",
                    stroke="#8884d8",
                    fill="#8884d8",
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                rx.recharts.tooltip(),
                data=State.chart_data,
                width="100%",
                height=300,
            ),

            rx.divider(margin_y="2em"),

            # Inventory Table
            rx.heading("Inventory Logic (Next 10 Days)", size="5"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Date"),
                        rx.table.column_header_cell("Predicted Demand"),
                        rx.table.column_header_cell("Suggested Stock (1.2x)"),
                    )
                ),
                rx.table.body(
                    rx.foreach(
                        State.df,
                        lambda row: rx.table.row(
                            rx.table.cell(row["ds"]),
                            rx.table.cell(row["yhat"].round(2)),
                            rx.table.cell((row["yhat"] * 1.2).round(2)),
                        ),
                    )
                ),
                width="100%",
            ),
            width="100%",
            padding_y="2em",
        ),
        on_mount=State.load_data,
    )

app = rx.App()
app.add_page(index)