import numpy as np
import pandas as pd

df = pd.read_csv("Database/data_csv_format.csv")
financial_df = pd.read_csv("Database/financial_data.csv")

for i, f_coun in df['foreign_country'].items():
    financial_df.at[i, '[for-coun]'] = f_coun

financial_df.to_csv('Database/financial_data.csv', index=False)