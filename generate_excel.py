import pandas as pd
import json

# Open the JSON file in read mode
# with open('/home/cyan/sesa/regions.json', 'r') as json_file:
#     # Parse the JSON data into a Python dictionary
#     pass
    # data = json.load(json_file)

# Create an empty list to store DataFrames for each region

region_dataframes = []

data = {
    "Region2": {
        "Comunidad": 8,
        "Unidades primer nivel": 8,
        "Unidades segundo nivel": 8,
        "Centros": 8
    },
    "Region1": {
        "Comunidad": 40,
        "Unidades primer nivel": 40,
        "Unidades segundo nivel": 40,
        "Centros": 40
    }
}


