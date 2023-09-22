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
    """
    This line uses the print function to output information about the type of the status_data variable. Here's the breakdown:

    \t: This is an escape sequence that represents a tab character. It adds an indentation to make the output visually organized.
    - type: <class 'str'>: This part of the output indicates that the type of status_data is a string. 
    The text is formatted as a label ("type") followed by the actual data ("<class 'str'>"). 
    The use of angle brackets (< and >) is a common convention in Python to indicate the type of an object.
    """
    print("\t- content:", status_data)
    """
    This line uses the print function to display the content of the status_data variable. Here's the breakdown:

    \t: Similar to the previous line, this adds a tab indentation for better readability.
    - content:: This part of the output is another label ("content") that indicates the data that follows is the content of status_data.
    status_data: This is the actual content of the status_data variable, which is printed next to the "content" label.
    """

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    status_data = fetch_status(url)
    print_status(status_data)
