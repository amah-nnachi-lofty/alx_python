#!/usr/bin/python3

"""
This Python script takes a URL as a command-line argument, sends a GET request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints an error message with the status code.

Usage:
    python script.py <URL>

Example:
    python script.py https://example.com
"""

import requests
import sys

""" Send a GET request to the URL provided as a command-line argument"""
response = requests.get(sys.argv[1])

""" Check if the HTTP status code indicates an error (greater than or equal to 400)"""
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    """ Print the response body if the status code is not an error"""
    print(response.text)
