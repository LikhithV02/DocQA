from faker import Faker
import pandas as pd
import numpy as np 
# Create an instance of Faker
fake = Faker('en_US')

# Generate 1000 USA zip codes
us_zip_codes = [fake.zipcode() for _ in range(1000)]

# Print the generated zip codes

df = pd.read_csv('Database/financial_data.csv')
for i , code in enumerate(us_zip_codes):
    df.at[i, '[zip1]'] = code  
shuffled_zip = df['[zip1]'].sample(frac=1).reset_index(drop=True)
df['[zip2]'] = shuffled_zip
df.to_csv("Database/financial_data.csv", index=False)
print(sum(df['[zip1]'] == df['[zip2]']))