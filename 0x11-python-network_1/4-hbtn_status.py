#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    # Fetch the URL
    response = requests.get("https://alx-intranet.hbtn.io/status")

    # Get the content as a string
    content = response.text

    # Print the results in the specified format
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
