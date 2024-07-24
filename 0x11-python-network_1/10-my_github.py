#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your user ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the username and token from the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, password)
    )

    try:
        # Try to parse the response as JSON
        json_response = response.json()
        # Print the user ID if available, else print None
        print(json_response.get('id'))
    except ValueError:
        # If the JSON is invalid, display an error message
        print("Not a valid JSON")
