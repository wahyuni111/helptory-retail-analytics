import pandas as pd

class Inventory:
    def __init__(self, inventory_df):
        self.inventory_df = inventory_df

    def get_restock_products(self):
        restock_products = self.inventory_df[
            self.inventory_df["Current Stock"]
            <=
            self.inventory_df["Minimum Stock"]
        ]
        return restock_products