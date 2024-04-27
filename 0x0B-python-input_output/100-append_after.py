#!/usr/bin/python3
"""defining append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific string."""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

