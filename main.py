import csv
import json
import os

# Prompt user for input and output filenames
input_file = input("Enter the path to your CSV file: ").strip()
output_file = input("What should the JSON file be named? ").strip()

# Ensure .json extension
if not output_file.endswith('.json'):
    output_file += '.json'

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"File '{input_file}' not found.")
    exit(1)

# Read and merge CSV rows
merged = {}
with open(input_file, mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        key = (
            row['State'],
            row['Grade'],
            row['Standard ID'],
            row['Standard Text'],
            row['Course Name']
        )
        if key not in merged:
            merged[key] = {
                "State": row['State'],
                "Grade": row['Grade'],
                "Standard ID": row['Standard ID'],
                "Standard Text": row['Standard Text'],
                "Course Name": row['Course Name'],
                "Project Name": [row['Project Name']]
            }
        else:
            if row['Project Name'] not in merged[key]["Project Name"]:
                merged[key]["Project Name"].append(row['Project Name'])

# Write merged data to JSON
with open(output_file, mode='w', encoding='utf-8') as json_file:
    json.dump(list(merged.values()), json_file, indent=4)

print(f"Converted '{input_file}' to '{output_file}' successfully.")
