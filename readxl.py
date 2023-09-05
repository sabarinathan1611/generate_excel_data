import pandas as pd

# Replace 'your_file.xlsx' with the actual filename and path
file_path = '01-08-23.xlsx'

# Read all sheets in the Excel file
sheet_names = pd.ExcelFile(file_path).sheet_names

# Create a dictionary to store data from all sheets
sheet_data_dict = {}

# Columns to extract
columns_to_extract = ["Shift", "A. InTime", "A.OutTime"]

# Loop through each sheet and read data
for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name, engine='openpyxl', skiprows=1)
    
    sheet_columns = df.columns.tolist()
    
    extracted_data = {}
    for column in columns_to_extract:
        if column in sheet_columns:
            extracted_data[column] = df[column].tolist()
        else:
            extracted_data[column] = None
    
    sheet_data_dict[sheet_name] = extracted_data

# Display the extracted data from each sheet
for sheet_name, extracted_data in sheet_data_dict.items():
    print(f"Sheet: {sheet_name}")
    for column, data in extracted_data.items():
        if data is not None:
            print(f"{column}: {data}")
        else:
            print(f"{column} not found in this sheet.")
    print("\n")