#!/usr/bin/python3
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Check if the file exists
filename = "add_item.json"
if path.exists(filename):
    # Load existing items from file
    items = load_from_json_file(filename)
else:
    items = []

# Add new items from command line arguments
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)

