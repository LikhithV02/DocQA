import numpy as np
import pandas as pd

df = pd.read_csv("Dataset_preparation/Database/data_csv_format.csv")
financial_df = pd.read_csv("Dataset_preparation/Database/financial_data.csv")
print(df['caledar_year'])
for i, year in df['caledar_year'].items():
    financial_df.at[i, '[year]'] = str(year)
financial_df.to_csv("Dataset_preparation/Database/financial_data.csv", index=False)