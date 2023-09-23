#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

def get_request(url):
    """
    Sends a GET request to the given URL.

    Args:
        url: The URL to send a GET request to.

    Returns:
        The response text from the server.
    """

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    return response.text


if __name__ == "__main__":
    url = sys.argv[1]
    response_text = get_request(url)
    print(response_text)
