'''
Cluster 0 fast moving 
cluster 1 slow moving'''
import pandas as pd

class ProductClustering:

    def __init__(self, sales_df):
        self.sales_df = sales_df


    def prepare_features(self):
        df = self.sales_df.copy()
        #format tanggal 
        df["Date"] = pd.to_datetime(
            df["Date"]
        )
        #total terjual
        total_sold = (

            df.groupby(
                "Product Name"
            )["Quantity"]
            .sum()
            .reset_index()

        )

        total_sold.columns = [

            "Product Name",
            "Total Sold"

        ]

        # =========================
        # DAILY SALES
        # =========================

        daily_sales = (

            df.groupby(
                ["Date", "Product Name"]
            )["Quantity"]
            .sum()
            .reset_index()

        )

        # =========================
        # AVERAGE SALES
        # =========================

        average_sales = (

            daily_sales.groupby(
                "Product Name"
            )["Quantity"]
            .mean()
            .reset_index()

        )

        average_sales.columns = [

            "Product Name",
            "Average Daily Sales"

        ]

        # =========================
        # MERGE
        # =========================

        features_df = pd.merge(

            total_sold,
            average_sales,
            on="Product Name"

        )

        features_df[
            "Average Daily Sales"
        ] = (

            features_df[
                "Average Daily Sales"
            ]
            .round(2)

        )

        return features_df