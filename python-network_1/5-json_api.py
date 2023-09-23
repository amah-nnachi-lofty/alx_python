#!/usr/bin/python3

import requests
import sys

def search_user(letter):
    try:
        """ Define the URL"""
        url = "http://0.0.0.0:5000/search_user"

        """ Prepare the data to send in the POST request"""
        data = {'q': letter}

        """ Send a POST request to the URL with the letter as a parameter"""
        response = requests.post(url, data=data)

        """ Check if the response contains valid JSON and is not empty"""
        if response.headers.get('content-type') == 'application/json' and response.json():
            user_data = response.json()
            user_id = user_data.get('id')
            user_name = user_data.get('name')
            print(f"[{user_id}] {user_name}")
        elif response.headers.get('content-type') == 'application/json':
            print("No result")
        else:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        sys.exit(1)

if __name__ == "__main__":
    """ Get the letter from the command-line arguments or set it to an empty string if not provided"""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    """ Call the search_user function with the letter"""
    search_user(letter)
