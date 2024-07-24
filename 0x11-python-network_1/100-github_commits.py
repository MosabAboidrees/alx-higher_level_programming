#!/usr/bin/python3
"""
This script takes a repository name and an owner name
and uses the GitHub API to list the 10 most recent commits
of the specified repository by the specified owner.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the repository name and owner name from the command-line arguments
    repo = sys.argv[1]
    owner = sys.argv[2]

    # Build the URL for the GitHub API request
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Parse the JSON response
    commits = response.json()

    # Print the 10 most recent commits
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author}')
