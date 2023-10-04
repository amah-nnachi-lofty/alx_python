#!/usr/bin/python3
"""
Starts a Flask web application with two routes and one dynamic route:
    / displays "Hello HBNB!"
    /hbnb displays "HBNB"
    /c/<text> captures a text parameter from the URL and displays "C " followed by the processed text.
 It include a dynamic routes:
    The /c/<text> route is a dynamic route. Whatever text you provide after /c/ in the URL, 
    it will be captured as a variable named text and passed to the c function. 
    The function then returns "C " followed by the value of the text variable, with underscores replaced by spaces.
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
    Display "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C " + escape(text.replace('_', ' '))
    """Replaces all occurrences of the underscore character (`_`) in the `text` variable with a space character (` `). 
        This is achieved using the `replace()` method on the `text` string.
    Concatenates the string "C " to the beginning of the escaped and modified `text` string using the `+` operator.
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
