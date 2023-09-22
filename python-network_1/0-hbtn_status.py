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
        dict: A dictionary containing the status information, or None on failure.

    Example:
        status_data = fetch_status("https://alu-intranet.hbtn.io/status")
        if status_data:
            print_status(status_data)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  
        """Raise an exception if the request was not successful"""

        if response.headers.get('content-type') == 'application/json':
            data = response.json()
            return data
        else:
            print("Received a non-JSON response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

def print_status(status_data):
    """
    Displays the status information with tabulation.

    Args:
        status_data (dict): A dictionary containing the status information.

    Example:
        print_status(status_data)
    """
    if status_data is not None:
        print("Body response:")
        print("\t- type:", type(status_data))
        print("\t- content:", status_data)
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    status_data = fetch_status(url)
    if status_data:
        print_status(status_data)
