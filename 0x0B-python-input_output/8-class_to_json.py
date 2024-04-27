#!/usr/bin/python3
"""defining class_to_json function"""

def class_to_json(obj):
    """Converts an object to a dictionary suitable for JSON serialization."""
    # Initialize an empty dictionary
    json_dict = {}

    # Get all attributes of the object
    attributes = obj.__dict__

    # Iterate through attributes
    for key, value in attributes.items():
        # Check if the value is of a simple data type (list, dict, str, int, bool)
        if isinstance(value, (list, dict, str, int, bool)):
            # Add the key-value pair to the dictionary
            json_dict[key] = value

    return json_dict

