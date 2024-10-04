import json
import csv
import pandas as pd

# Read file responseoutput.txt into a string
with open('response_output_new.txt', 'r') as file:
    response_data = file.read()

# Load JSON data
json_data = json.loads(response_data)

data = json_data['tables']

# Extracting the headers and rows
all_tables = ['tab0', 'tab1', 'tab2', 'tab3', 'tab4', 'tab5', 'tab6', 'tab7', 'tab8', 'tab9']

for table_name in all_tables:
    table_data = data[table_name]
    headers = [value for key, value in table_data["lin0"].items()]
    rows = []

    for key in table_data:
        if key != "lin0":  # Skip the header line
            row = [value for value in table_data[key].values()]
            rows.append(row)

    # Creating a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Display the DataFrame
    print(f"Table: {table_name}")
    print(df)
    print("\n")

    # Write to CSV
    df.to_csv(f'{table_name}_classe_ekho_output.csv', index=False, sep=';', encoding='utf-8-sig')
