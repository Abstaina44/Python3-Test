/Users/abstaina/Desktop/Screenshot\ 2023-07-19\ at\ 12.04.17\ AM.png

 #!/usr/bin/python3
"""
This program converts dictionaries to JSON
"""


import json


def to_json_string(my_obj):
    """
    Convert a dict to JSON format
    Args:
     - my_obj: dict
    """

    return (json.dumps(my_obj))
