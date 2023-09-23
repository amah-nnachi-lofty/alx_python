#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

response = requests.get(sys.argv[1])

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)