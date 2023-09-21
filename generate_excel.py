import pandas as pd
import itertools
import json

# Open the JSON file for reading
with open('regions.json', 'r') as json_file:
    # Load the JSON data into a Python dictionary
    data = json.load(json_file)

# Now, 'data' contains the JSON data as a Python dictionary
print(data)

data = {"Region1": {'Comunidad': ['Alice', 'Bob', 'Charlie'],
                    'Unidades primer nivel': [20, 30, 35],
                    'Unidades segundo nivel': [0, 0, 0],
                    'Centro / Servicios / Modulos/ Esp': [0, 0, 0]},
        "Region2": {'Comunidad': ['Alice', 'Bob', 'Charlie'],
                    'Unidades primer nivel': [20, 30, 35],
                    'Unidades segundo nivel': [0, 0, 0],
                    'Centro / Servicios / Modulos/ Esp': [0, 0, 0]}}

first_key = next(iter(data))
print(first_key)
# second_key = next(iter(data))
# print(second_key)
keys_iterator = iter(data)

# Use itertools.islice to skip the first key and get the second
second_key = next(itertools.islice(keys_iterator, 1, 2))

print(second_key)

table_width = 5

df1 = pd.DataFrame(data["Region1"])

df2 = pd.DataFrame(data["Region2"])

# Specify the numeric columns to sum
columns_to_sum = ['Unidades primer nivel', 'Unidades segundo nivel', 'Centro / Servicios / Modulos/ Esp']

# Calculate row-wise sum for the numeric columns and add it as a new column
df1['Total'] = df1[columns_to_sum].sum(axis=1)
df2['Total'] = df1[columns_to_sum].sum(axis=1)

# Specify the Excel file name
excel_file = 'example.xlsx'

initial_cords = [1, 1]
gap = 1
# cords = [0, 0]

# Create a Pandas Excel writer object
with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
    # Write the DataFrame to the Excel file starting at cell B2
    df1.to_excel(writer, sheet_name='Septiembre', index=False, startrow=initial_cords[0], startcol=initial_cords[1])
    df1.to_excel(writer, sheet_name='Septiembre', index=False, startrow=initial_cords[0], startcol=initial_cords[1] + table_width + gap)
        # df1.to_excel(writer, sheet_name='Septiembre', index=False, )
    # Get the xlsxwriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Septiembre']
    worksheet.write_string(initial_cords[0] - 1, 0 + initial_cords[1] + int(table_width / 2), first_key)
    worksheet.write_string(initial_cords[0] - 1, 0 + initial_cords[1] + int(table_width / 2) + table_width + gap, second_key)


# Save the Excel file
writer._save()
