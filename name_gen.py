# import pandas as pd
# import random

# # Load US.csv and financial_data.csv
# us_df = pd.read_csv('US.csv')
# financial_df = pd.read_csv('financial_data.csv')



# # Select up to the minimum of 50000 or the number of rows in financial_df

# selected_names = us_df.iloc[:1000]
# # Combine first and last names into a single column
# selected_names['[payer_name]'] = selected_names['Chelsea'] + ' ' + selected_names['Mitchell']

# # Update the financial_df with selected names
# for i, row in selected_names.iterrows():
#    payer_name = row['[payer_name]']
#    print(payer_name)
#    if payer_name != ""or payer_name != None:
#         financial_df.at[i, '[payer_name]'] = payer_name

# # Save the updated financial_data.csv
# financial_df.to_csv('financial_data_updated.csv', index=False)

# print("Update complete. New financial data saved to financial_data_updated.csv")


import pandas as pd

# Load US.csv and financial_data.csv
us_df = pd.read_csv('Database/US.csv')
financial_df = pd.read_csv('Database/financial_data.csv')

# Select the first 1000 non-empty rows from us_df
selected_names = us_df.head(1000)

# Combine first and last names into a single column, handling missing values
selected_names['[payer_name]'] = selected_names['Chelsea'].fillna('') + ' ' + selected_names['Mitchell'].fillna('')
selected_names['[name]'] = selected_names["[payer_name]"].sample(frac=1).reset_index(drop=True)
# Filter out empty names
selected_names = selected_names[selected_names['[payer_name]'].str.strip() != ""]

# Update the financial_df with selected names
for i, payer_name in selected_names['[payer_name]'].items():    
    # Update only if payer_name is not empty
    if payer_name.strip() != "":
        financial_df.at[i, '[payer_name]'] = payer_name


# Save the updated financial_data.csv
financial_df["[name]"] = selected_names["[name]"]
print(sum(financial_df["[name]"] == financial_df["[payer_name]"]))
financial_df.to_csv('Database/financial_data.csv', index=False)

print("Update complete. New financial data saved to financial_data_updated.csv")
