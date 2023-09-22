"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a GET request to the specified URL and displays the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Example:
        python script.py https://example.com
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(f"The value of X-Request-Id header is: {x_request_id}")
        else:
            print("X-Request-Id header is not present in the response.")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
