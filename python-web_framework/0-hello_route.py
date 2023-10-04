#!/usr/bin/python3
"""
The script creates a Flask web application, defines a route to handle requests to the root URL ("/"), 
and starts the Flask development server to handle incoming requests. 
This allows the "Hello HBNB!" message to be displayed when accessing the root URL of the application
"""

"""Import Flask class from Flask module"""
from flask import Flask
"""Create a Flask web application instance"""
app = Flask(__name__) 


"""
Define a route for the root URL ('/')
strict_slashes=False allows the route to be matched with or without a trailing slash
Only one route, /, which displays the message "Hello HBNB!".
"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when accessing root URL.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    """This line checks whether the script is being run directly by the Python interpreter 
    or if it is being imported as a module into another script. 
    When a Python script is run, the special variable __name__ is set to '__main__'. 
    If the script is being imported, __name__ will be set to the name of the module.

    To accept connections from any IP address (0.0.0.0) on the host machine
    """
    app.run(host='0.0.0.0', port=5000)
