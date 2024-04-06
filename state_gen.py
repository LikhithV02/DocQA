import random
import pandas as pd
from faker import Faker

fake = Faker('en_US')

# List of all 50 states in the USA
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
    "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]
state_abb = []
for _ in range(1000):
    state_abb.append(fake.state_abbr())
# Generate 1000 random states
random_states_1 = random.choices(states, k=1000)
financial_df = pd.read_csv('Database/financial_data.csv')

for i, state1 in enumerate(random_states_1):
    # df.at[country2[0],"[country1]"] = country1
    financial_df.at[i,"[state1]"] = state1
shuffled_states = financial_df["[state1]"].sample(frac=1).reset_index(drop=True)

financial_df['[state2]'] = shuffled_states
financial_df['[state3]'] = state_abb
print(sum(financial_df["[state1]"] == financial_df["[state2]"]))
financial_df.to_csv("Database/financial_data.csv",index=False)
# Print the random states
# for state in random_states:
#     print(state)
