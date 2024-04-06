import pandas as pd
import numpy as np

df = pd.read_csv("Database/data_csv_format.csv")
financial_df = pd.read_csv("Database/financial_data.csv")

for i, address in df['payers_add'].items():
    financial_df.at[i, '[street_addr]'] = address
financial_df['[Address]'] = df['rec_street']
financial_df.to_csv("Database/financial_data.csv", index=False)
