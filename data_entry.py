import tkinter as tk
import json
import os
import pandas as pd

# Define the path to the JSON file
json_file_path = 'regions.json'

# Create an empty dictionary to store region data
region_data = {}

# Define the dropdown options for the "Region" field
region_options = ["Region1", "Region2", "Region3", "Region4", "Region5"]

# Load existing data from the JSON file (if it exists)
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        region_data = json.load(json_file)

def save_data():
    region_name = region_name_variable.get()  # Get the selected region from the dropdown
    
    data = {
        'Comunidad': int(comunidad_entry.get()),
        'Unidades primer nivel': int(uni_primer_nivel_entry.get()),
        'Unidades segundo nivel': int(uni_segundo_nivel_entry.get()),
        'Centros': int(centros_entry.get())
    }
    
    # Update the region data with the new entry
    if region_name in region_data:
        # If the region already exists, update the data
        region_data[region_name].update(data)
    else:
        # If the region doesn't exist, create a new entry
        region_data[region_name] = data
    
    with open(json_file_path, 'w') as json_file:
        json.dump(region_data, json_file, indent=4)
    
    # Clear the entry fields
    region_name_variable.set("")  # Clear the selected region in the dropdown
    comunidad_entry.delete(0, tk.END)
    uni_primer_nivel_entry.delete(0, tk.END)
    uni_segundo_nivel_entry.delete(0, tk.END)
    centros_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Data Entry App')

# Dropdown for Region
region_name_label = tk.Label(root, text='Region Name:')
region_name_label.pack()

# Create a variable to store the selected region
region_name_variable = tk.StringVar(root)
region_name_variable.set(region_options[0])  # Set the default value
region_dropdown = tk.OptionMenu(root, region_name_variable, *region_options)
region_dropdown.pack()

comunidad_label = tk.Label(root, text='Comunidad:')
comunidad_label.pack()
comunidad_entry = tk.Entry(root)
comunidad_entry.pack()

uni_primer_nivel_label = tk.Label(root, text='Unidades primer nivel:')
uni_primer_nivel_label.pack()
uni_primer_nivel_entry = tk.Entry(root)
uni_primer_nivel_entry.pack()

uni_segundo_nivel_label = tk.Label(root, text='Unidades segundo nivel:')
uni_segundo_nivel_label.pack()
uni_segundo_nivel_entry = tk.Entry(root)
uni_segundo_nivel_entry.pack()

centros_label = tk.Label(root, text='Centros:')
centros_label.pack()
centros_entry = tk.Entry(root)
centros_entry.pack()

save_button = tk.Button(root, text='Save Data', command=save_data)
save_button.pack()

root.mainloop()
