from faker import Faker
import pandas as pd

# Create an instance of the Faker class
fake = Faker()

# Function to generate state identification numbers
def generate_state_ids(num):
    state_ids = []
    for _ in range(num):
        state_id = fake.ssn()
        state_ids.append(state_id)
    return state_ids

# Generate 1000 state identification numbers
state_ids = generate_state_ids(1000)


financial_df = pd.read_csv("Database/financial_data.csv")

for i, id in enumerate(state_ids):
    financial_df.at[i, '[s-no]'] = id

financial_df.to_csv("Database/financial_data.csv", index=False)