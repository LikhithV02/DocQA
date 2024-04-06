
import pandas as pd
import numpy as np
from faker import Faker



fake = Faker()
fake.add_provider("faker.providers.bank")

acc_list = []
for _ in range(1000):
    acc_list.append(fake.bban())

df = pd.read_csv("Database/financial_data.csv")
for i , data in enumerate(acc_list):
    df.at[i,"[account]"] = data
# df["[account]"] = acc_list
df.to_csv("Database/financial_data.csv", index=False)

