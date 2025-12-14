#!/usr/bin/python3
"""Script that ad uments to a Python list and saves them to a JSON file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing list from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with an empty list
    items = []

# Add all command-line arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
