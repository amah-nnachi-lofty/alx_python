#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

url = sys.argv[1]
"""
 sys.argv list contains the command-line arguments passed to the script. 
 sys.argv[0] is the script's name, and sys.argv[1] is the first argument (in this case, the URL).
"""

req = requests.get(url)
"""
This line sends an HTTP GET request to the URL specified in url using the requests.get() method. 
The response from the server is stored in the req variable.
"""
print(req.headers.get('X-Request-Id'))
"""
This accesses the headers of the HTTP response, which is stored in the req variable.
.get('X-Request-Id'): This method retrieves the value associated with the X-Request-Id header from the response headers.
It extracts and prints the value of the X-Request-Id header from the response.
"""