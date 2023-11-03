import csv, json

if __name__ == "__main__":

    # Read the CSV file
    csv_file_path = str(input("Enter the path to the CSV file: "))
    json_file_path = str(input("Enter the path to the JSON file: "))

    data = {}
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data[row["id"]] = row

    with open(json_file_path, "w") as json_file:
        json_file.write(json.dumps(data, indent=4))
