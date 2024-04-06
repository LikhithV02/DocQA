import pandas as pd
import numpy as np
import random

fin_df = pd.read_csv('Database/financial_data.csv')
df = pd.read_csv('Database/citys.csv')
new_city = df['PlaceName']
new_city = new_city.to_list()
print(new_city)

random_cities = random.choices(new_city, k=1000)
for i, city in enumerate(random_cities):
    fin_df.at[i, '[city1]'] = city


shuffled_city2 = fin_df['[city1]'].sample(frac=1).reset_index(drop=True)
fin_df['[city2]'] = shuffled_city2
fin_df.to_csv("Database/financial_data.csv", index=False)
print(sum(fin_df['[city1]'] == fin_df['[city2]']))