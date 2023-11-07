import csv
import json

# Define the input and output file names
csv_file = 'random_walk.csv'
json_file = 'output.json'

# Read data from the CSV file and convert to float
data = []
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.extend([float(value) for value in row])

# Create a dictionary with a key and the data as a list of numbers
data_dict = {
    "data": data
}

# Write the dictionary to a JSON file
with open(json_file, 'w') as jsonfile:
    json.dump(data_dict, jsonfile, indent=2)

print(f'Data from {csv_file} has been written to {json_file}.')
