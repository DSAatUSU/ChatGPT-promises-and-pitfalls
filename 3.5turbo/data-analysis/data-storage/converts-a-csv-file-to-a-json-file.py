import csv
import json

def convert_csv_to_json(csv_file, json_file):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Write the JSON file
    with open(json_file, 'w') as file:
        json.dump(rows, file, indent=4)

# Run the conversion
csv_file = 'input.csv'
json_file = 'output.json'
convert_csv_to_json(csv_file, json_file)
