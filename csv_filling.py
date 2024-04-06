from docx import Document
import csv
from tqdm import tqdm
import random
from faker import Faker
import pandas as pd
import string

financial_df = pd.read_csv('Database/financial_data.csv')
# Example usage
years = [str(year) for year in range(2000, 2026)]  # From 2000 to 2025
company_initials = ["ABC", "XYZ", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZA"]
words = ['D','E', 'F', 'S', 'G', 'H', 'AA', 'EE', 'BB']


def generate_routing_number():
    for i in range(1000):
        routing_number = ""
        for _ in range(9):
            routing_number += str(random.randint(0, 9))
        financial_df.at[i,"[RTN]"] = routing_number
    financial_df.to_csv("Database/financial_data.csv",index=False)

def generate_cusip():
    for i in range(1000):
        # Generate the first 6 characters (letters and digits)
        first_six = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        
        # Generate the last digit (check digit)
        weighted_sum = sum([(ord(char) - ord('0')) * (2 if i % 2 else 1) for i, char in enumerate(first_six[::-1])])
        check_digit = (10 - (weighted_sum % 10)) % 10
        
    
        val = first_six + str(check_digit)
        financial_df.at[i,"[CUSIP]"] = val
    financial_df.to_csv("Database/financial_data.csv",index=False)


def generate_random_number():
    for i in range(1000):
        val = random.randint(1, 10)
        financial_df.at[i,"[FORM]"] = val
    financial_df.to_csv("Database/financial_data.csv",index=False)
    




def generate_fax_number():
    for i in range(1000):
        country_code = random.choice(['+1', '+44', '+61', '+81', '+86'])  # Example country codes
        area_code = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        exchange_code = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        subscriber_number = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        val = f"{country_code} ({area_code}) {exchange_code}-{subscriber_number}"
        financial_df.at[i,"[FAX]"] = val
    financial_df.to_csv("Database/financial_data.csv",index=False)
    




def generate_fake_email():
    for i in range(1000):
        fake = Faker()
        val = fake.email()
        financial_df.at[i,"[EMAIL]"] = val
    financial_df.to_csv("Database/financial_data.csv",index=False)


def generate_control_number(years, company_initials):
    for i in range(1000):
        year = random.choice(years)
        initials = random.choice(company_initials)
        batch_number = random.randint(1, 999)
        control_number = f"{year}-{initials.upper()}-{str(batch_number).zfill(3)}"
        financial_df.at[i,"[ACN]"] = control_number
    financial_df.to_csv("Database/financial_data.csv",index=False)
    

def generate_codes():
    for i in range(1000):
        random_values = random.sample(words, 4)
        financial_df.at[i,"[code_1]"] = random_values[0]
        financial_df.at[i,"[code_2]"] = random_values[1]
        financial_df.at[i,"[code_3]"] = random_values[2]
        financial_df.at[i,"[code_4]"] = random_values[3]
    financial_df.to_csv("Database/financial_data.csv",index=False)
    
        


if __name__ == "__main__":
    # generate_routing_number()
    # generate_control_number(years, company_initials)
    # generate_cusip()
    # generate_fake_email()
    # generate_fax_number()
    # generate_random_number()
    generate_codes()