"""
Fetches the status of the alu-intranet.hbtn.io service and displays it in a tabulated format.

Returns:
    None
"""

import requests


def fetch_status():
    """Fetches the status of the alu-intranet.hbtn.io service.

    Returns:
        A JSON object containing the status of the service.
    """

    response = requests.get('https://alu-intranet.hbtn.io/status')
    if response.status_code != 200:
        raise Exception('Failed to fetch status: {}'.format(response.status_code))
    return response.json()


def display_status(status):
    """Displays the status of the alu-intranet.hbtn.io service in a tabulated format.

    Args:
        status: A JSON object containing the status of the service.
    """

    print('Status:')
    for key, value in status.items():
        print('\t- {}: {}'.format(key, value))


if __name__ == '__main__':
    status = fetch_status()
    display_status(status)
