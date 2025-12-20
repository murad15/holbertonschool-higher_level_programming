#!/usr/bin/env python3
def serialize_and_save_to_file(data, filename):
    # Your code here to load and deserialize data from the specified file  
    with open(filename, "w") as outfile: 
        json.dump(data, outfile, indent=4)

def load_and_deserialize(filename):
    with open('data.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    data = json.load(f)
