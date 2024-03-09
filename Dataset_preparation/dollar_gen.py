import random
import pandas as pd
import numpy as np

df = pd.read_csv("Database/data_csv_format.csv")
financial_df = pd.read_csv("Database/financial_data.csv")

for i, a_1 in df['one_a'].items():
    financial_df.at[i, '[od]'] = a_1
financial_df['[q-div]'] = df['one_b']
financial_df['[t-cap]'] = df['to_a']
financial_df['[unr]'] = df['to_b']
financial_df['[sec-12]'] = df['to_c']
financial_df['[Coll]'] = df['to_d']
financial_df['[sec-897]'] = df['to_e']
financial_df['[sec-897-gain]'] = df['to_f']
financial_df['[N-dis]'] = df['three']
financial_df['[fed-in]'] = df['four']
financial_df['[Sec-199]'] = df['five']
financial_df['[inves]'] = df['six']
financial_df['[For-tax]'] = df['seven']
financial_df['[cash-dis]'] = df['nine']
financial_df['[n-cash]'] = df['ten']
financial_df['[exem-div]'] = df['twle']
financial_df['[spec]'] = df['trten']
financial_df['[s-t-w]'] = df['sixten']
financial_df.to_csv('Database/financial_data.csv', index=False)