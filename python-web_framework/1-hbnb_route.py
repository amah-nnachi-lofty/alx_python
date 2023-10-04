#!/usr/bin/python3
"""
script that starts a Flask web application to handle different URL:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    Use the option strict_slashes=False in your route definition

"""

from flask import Flask
app = Flask(__name__)


"""
Route handler 1: for the root URL '/'. http://localhost:5000: Display the message "Hello HBNB!".
"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when accessing root URL.
    """
    return "Hello HBNB!"

"""Route handler 2: for the URL '/hbnb'. http://localhost:5000/hbnb: Display the message "HBNB"
"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when accessing '/hbnb' URL.
    """
    return "HBNB"

if __name__ == '__main__':
    """
    The main entry point of the script to start the Flask web app.
    """
    app.run(host='0.0.0.0', port=5000)
