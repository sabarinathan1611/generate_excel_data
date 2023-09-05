import pandas as pd
import random
import faker

# Initialize the Faker generator
fake = faker.Faker()

# Create a list of possible shift types
shift_types = ["8G", "8A", "8C", "8B", "GS", "12A", "12B", "10A"]

# Create a list of possible designations
designations = ["Manager", "Supervisor", "Engineer", "Technician", "Assistant"]

# Create a list of possible work types
work_types = ["Full-time", "Part-time", "Contract", "Temporary"]

# Number of sheets and entries per sheet
num_sheets = 35
entries_per_sheet = 1000

# Create an Excel writer object
excel_file_path = "employee_data.xlsx"
excel_writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

# Generate data and create sheets
for sheet_number in range(num_sheets):
    data_list = []
    for _ in range(entries_per_sheet):
        data = {
            "name": fake.name(),
            "dob": fake.date_of_birth().strftime("%Y-%m-%d"),
            "designation": random.choice(designations),
            "workType": random.choice(work_types),
            "email": fake.email(),
            "phoneNumber": fake.phone_number(),
            "adharNumber": fake.random_int(min=100000000000, max=999999999999),
            "gender": random.choice(["Male", "Female"]),
            "address": fake.address(),
            "shift": random.choice(shift_types)
        }
        data_list.append(data)

    # Create a DataFrame from the list of data
    df = pd.DataFrame(data_list)

    # Save the DataFrame to an Excel sheet with a unique name
    sheet_name = f"Sheet_{sheet_number + 1}"
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

# Save the Excel file
excel_writer.save()

print(f"{num_sheets} Excel sheets created with {entries_per_sheet} entries each in '{excel_file_path}'.")

