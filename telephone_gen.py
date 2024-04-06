from faker import Faker
import pandas as pd
import numpy as np

import re

def generate_fake_usa_phone_numbers(count=1000):
    fake = Faker('en_US')
    phone_numbers = []
    for _ in range(count):
        # Generate a phone number
        phone_number = fake.phone_number()
        # Remove 'x' and any subsequent digits after it
        phone_number = re.sub(r'x\d+', '', phone_number)
        phone_numbers.append(phone_number)
    return phone_numbers



# Generate 1000 fake USA phone numbers
fake_phone_numbers = generate_fake_usa_phone_numbers(count=1000)
print(fake_phone_numbers)

# Print the fake phone numbers
df = pd.read_csv('  Database/financial_data.csv')

for i, no in enumerate(fake_phone_numbers):
    df.at[i,'[telephone]'] = no
df.to_csv('Database/financial_data.csv', index=False)