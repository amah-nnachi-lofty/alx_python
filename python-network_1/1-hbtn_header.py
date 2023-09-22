"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

def get_request_id(url):
  """Sends a request to the specified URL and returns the value of the `X-Request-Id` header in the response.

  Args:
    url: The URL to send a request to.

  Returns:
    The value of the `X-Request-Id` header in the response, or `None` if the header is not present.
  """

  response = requests.get(url)
  x_request_id = response.headers.get('X-Request-Id')
  return x_request_id

def main():
  """Takes in a URL from the user, sends a request to the URL, and displays the value of the `X-Request-Id` header in the response."""

  url = input('Enter a URL: ')

  # Check if the URL is empty
  if not url:
    print('No URL entered.')
    sys.exit(1)

  # Strip whitespace from the URL
  url = url.strip()

  # Correct spelling errors in the URL
  if url == 'Holberton school':
    url = 'Holberton School'

  x_request_id = get_request_id(url)

  if x_request_id is not None:
    print('The value of the `X-Request-Id` header in the response is: {}'.format(x_request_id))
  else:
    print('The `X-Request-Id` header is not present in the response.')

if __name__ == '__main__':
  main()
