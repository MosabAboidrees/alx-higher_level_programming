# 0x10. Python - Network #0

## Description
This project covers various tasks related to network programming using Bash and Python. It includes tasks that involve sending HTTP requests, handling JSON data, and more. Each task focuses on different aspects of network programming, using tools like `curl` and following specific constraints.

## Tasks

### Task 0: cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

- File: `0-body_size.sh`
- Usage: `./0-body_size.sh <URL>`

### Task 1: cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. Display only the body of a 200 status code response.

- File: `1-body.sh`
- Usage: `./1-body.sh <URL>`

### Task 2: cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

- File: `2-delete.sh`
- Usage: `./2-delete.sh <URL>`

### Task 3: cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- File: `3-methods.sh`
- Usage: `./3-methods.sh <URL>`

### Task 4: cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`.

- File: `4-header.sh`
- Usage: `./4-header.sh <URL>`

### Task 5: cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com`. A variable `subject` must be sent with the value `I will always be here for PLD`.

- File: `5-post_params.sh`
- Usage: `./5-post_params.sh <URL>`

### Task 6: Find a peak
Write a function that finds a peak in a list of unsorted integers.

- File: `6-peak.py`
- Usage: The function can be tested with the provided `6-main.py` script.
- Complexity: `O(log(n))`

### Task 7: Only status code
Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.

- File: `100-status_code.sh`
- Usage: `./100-status_code.sh <URL>`

### Task 8: cURL a JSON file
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. The script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.

- File: `101-post_json.sh`
- Usage: `./101-post_json.sh <URL> <file>`

### Task 9: Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

- File: `102-catch_me.sh`
- Usage: `./102-catch_me.sh`

## Usage
To run any of the scripts, make sure they are executable. You can make a script executable with the following command:
```bash
chmod +x script_name.sh

