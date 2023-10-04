#!/usr/bin/python3
"""
Starts a Flask web application with specific routes, including dynamic routes and default values.
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)
"""A standard to indicate where to locate resources"""

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when accessing root URL.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when accessing '/hbnb' URL.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display "C ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C " + escape(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Display "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "Python " + escape(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
