#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

    You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
    The first argument will be your username
    The second argument will be your password (in your case, a personal access token as password)
"""

import requests
import sys

def get_github_user_id(username, access_token):
    """
    Get the GitHub user id for a given username.

    :param username: The GitHub username to get the user id for.
    :param access_token: The GitHub personal access token to authenticate the request.
    :return: The user id for the given username.
    """
    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data['id']
    else:
        raise Exception(f'Error: {response.status_code}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <GitHub Username> <Personal Access Token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    user_id = get_github_user_id(username, access_token)
    print(f'The GitHub user id for {username} is: {user_id}')
