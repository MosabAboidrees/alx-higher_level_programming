#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints: Error code: followed by the value of the HTTP status code.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Send a request to the URL
    response = requests.get(url)

    # Check if the HTTP status code is >= 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # Display the body of the response
        print(response.text)
