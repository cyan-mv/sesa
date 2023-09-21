import json

# Specify the full absolute path to the JSON file
file_path = '/home/cyan/sesa/regions.json'

# Open the JSON file in read mode
with open(file_path, 'r') as json_file:
    # Parse the JSON data into a Python dictionary
    data = json.load(json_file)

# Now you can work with the 'data' dictionary
print(data["region1"]["Comunidad"])
