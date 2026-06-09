#disini akan ada fast moving dan moving average
import pandas as pd


class Analytics:

    def __init__(self, sales_df):

        self.sales_df = sales_df
#FAST MOVING PRODUCTS

    def get_fast_moving_products(self):

        fast_moving = (

            self.sales_df
            .groupby("Product Name")["Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                by="Quantity",
                ascending=False
            )
            .head(10)

        )

        return fast_moving
 #AVERAGE DAILY SALES

    def get_average_daily_sales(self):

        df = self.sales_df.copy()

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

        daily_sales = (

            df.groupby(
                ["Date", "Product Name"]
            )["Quantity"]
            .sum()
            .reset_index()

        )

        average_sales = (

            daily_sales.groupby(
                "Product Name"
            )["Quantity"]
            .mean()
            .sort_values(
                ascending=False
            )

        )

        return average_sales