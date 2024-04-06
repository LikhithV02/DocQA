import csv

# Your financial_data dictionary
financial_data = {
    "[TIN_payer]": "1231263126",
    "[TIN_recipient]": "6541245425",
    "[payer_name]": " monish",
    "[street_addr]": "bangalore",
    "[city1]": "mysore",
    "[state1]": "karnataka",
    "[country1]": "indina",
    "[zip1]": "541353",
    "[telephone]": "8276752675",
    "[name]": "abhishek",
    "[Address]": "banshankari",
    "[city2]": "hyderabad",
    "[state2]": "delhi",
    "[country2]": "US",
    "[zip2]": "7656522",
    "[account]": "61251457125761257",
    "[od]": "232.74",
    "[q-div]": "3322.2",
    "[t-cap]": "21.36",
    "[year]": "2024",
    "[unr]": "231.42",
    "[sec-12]": "12.12",
    "[Coll]": "121.3",
    "[sec-897]": "123.3",
    "[sec-897-gain]": "8773.46",
    "[N-dis]": "122.4",
    "[fed-in]": "9378.3",
    "[Sec-199]": "524.2",
    "[inves]": "56425",
    "[For-tax]": "1243.43",
    "[for-coun]": "635.72",
    "[cash-dis]": "8716.72",
    "[n-cash]": "8267.2",
    "[exem-div]": "9252.2",
    "[spec]": "817.2",
    "[state3]": "Assam",
    "[s-no]": "22",
    "[s-t-w]": "623.36"
}

# Specify the CSV file name
csv_file = "Database/financial_data.csv"

# Writing to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=financial_data.keys())

    writer.writeheader()

print("CSV file has been created successfully.")
