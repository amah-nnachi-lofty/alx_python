#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

def send_request(url):
  """Sends a request to the specified URL and returns the response.

  Args:
    url: The URL to send a request to.

  Returns:
    A `Response` object containing the response from the server.
  """

  response = requests.get(url)
  return response

def display_response(response):
  """Displays the body of the response.

  Args:
    response: A `Response` object containing the response from the server.
  """

  print(response.content)

def main():
  """Takes in a URL from the user, sends a request to the URL, and displays the body of the response."""

  url = input('Enter a URL: ')

  """ Send a request to the URL"""
  response = send_request(url)

  """ Check the HTTP status code"""
  status_code = response.status_code

  """ If the HTTP status code is greater than or equal to 400, print an error message"""
  if status_code >= 400:
    print('Error code: {}'.format(status_code))
  else:
    """ Display the body of the response """
    display_response(response)

if __name__ == '__main__':
  main()
