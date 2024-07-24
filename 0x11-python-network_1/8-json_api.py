#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from the command-line arguments
    # If no argument is given, set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create the payload with the letter
    payload = {'q': q}

    # Send a POST request to the URL with the payload
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        # Check if the JSON is empty
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        # If the JSON is invalid, display an error message
        print("Not a valid JSON")
