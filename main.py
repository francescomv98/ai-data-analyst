from src.data_loader import DataLoader
from src.dataframe_manager import DataFrameManager

df = DataLoader.load_csv("data/sales.csv")

manager = DataFrameManager(df)

print(manager.get_average_revenue())

print(manager.get_top_products())

print(manager.get_best_region())

print(manager.get_monthly_revenue())