#!/usr/bin/python3

"""
Write a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
"""
 extract the URL and email address from the command-line arguments. 
 sys.argv[1] represents the first argument (the URL), and sys.argv[2] represents the second argument (the email address).
"""

response = requests.post(url, data={'email': email})
"""
sends a POST request to the specified URL (url) with the email address as a parameter. 
The email address is passed as a dictionary with the key 'email' and the value being the email address itself.
"""

print(response.text)
