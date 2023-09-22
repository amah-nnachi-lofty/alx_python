"""Fetches the status of the alu-intranet.hbtn.io service and displays the body response in the following format:

Body response:$
   - type: <class 'str'>$
   - content: OK$
"""
import requests

def fetch_status(url):
    """
    Fetches status information from a given URL using the requests package.

    Args:
        url (str): The URL to fetch status information from.

    Returns:
        str: The response content as a string, or an empty string on failure.

    Example:
        status_data = fetch_status("https://alu-intranet.hbtn.io/status")
        print_status(status_data)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful

        return response.text  # Return the response content as a string
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return ""

def print_status(status_data):
    """
    Displays the status information with tabulation.

    Args:
        status_data (str): The response content as a string.

    Example:
        print_status(status_data)
    """
    print("Body response:")
    print("\t- type: <class 'str'>")
    print("\t- content:", status_data)

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    status_data = fetch_status(url)
    print_status(status_data)
