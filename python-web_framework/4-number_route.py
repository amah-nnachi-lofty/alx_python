#!/usr/bin/python3
"""
Starts a Flask web application with specific routes, including dynamic routes, default values, and number route.
Captures an integer parameter from the URL and displays "n is a number" only if n is an integer
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

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
    formatted_text = escape(text.replace('_', ' '))
    return "C {}".format(formatted_text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Display "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    formatted_text = escape(text.replace('_', ' '))
    return "Python {}".format(formatted_text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
