#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument with the contents of a file passed as the second argument, and displays the body of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
