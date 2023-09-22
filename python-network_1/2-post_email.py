#!/usr/bin/python3

"""
Write a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email address as a parameter and displays the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter.

    Example:
        python script.py https://example.com user@example.com
    """
    try:
        """ Create a dictionary with the 'email' parameter"""
        data = {'email': email}

        """Send a POST request with the data """
        response = requests.post(url, data=data)

        """ Check for a successful response (status code 200)"""
        if response.status_code == 200:
            print("Response Body:")
            print(response.text)
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
