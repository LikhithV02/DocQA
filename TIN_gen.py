import pandas as pd
import numpy as np

# Load PIN.csv
pin_df = pd.read_csv('Database/PIN.csv')

# Load financial_data.csv
financial_df = pd.read_csv('Database/financial_data.csv')

# Shuffle the PINs once
shuffled_pins = pin_df.sample(frac=1).reset_index(drop=True)
shuffled_pins_2 = pin_df.sample(frac=1).reset_index(drop=True)
shuffled_pins['TIN_payer'] = shuffled_pins['Output']
shuffled_pins_2['TIN_recipient'] = shuffled_pins_2['Output']
# Update the financial_df with selected names
for payer_PIN, recipient_PIN in zip(shuffled_pins['TIN_payer'].items(), shuffled_pins_2['TIN_recipient'].items()):
    # Update only if payer_name is not empty
    if payer_PIN[1].strip() != "" or recipient_PIN[1].strip() != "":
        financial_df.at[payer_PIN[0], '[TIN_payer]'] = payer_PIN[1]
        financial_df.at[recipient_PIN[0], '[TIN_recipient]'] = recipient_PIN[1]
# Save the modified financial_data.csv
financial_df.to_csv('Database/financial_data.csv', index=False)

print(sum(shuffled_pins['TIN_payer'] == shuffled_pins_2['TIN_recipient']))


