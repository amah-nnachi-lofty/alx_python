#!/usr/bin/python3
"""
Starts a Flask web application with specific routes, including dynamic routes,
default values, and number_template and number_odd_or_even routes.
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when accessing root URL.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing '/hbnb' URL.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Displays "C ", followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    formatted_text = escape(text.replace('_', ' '))
    return "C {}".format(formatted_text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Displays "Python ", followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    formatted_text = escape(text.replace('_', ' '))
    return "Python {}".format(formatted_text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays "{} is a number" only if n is an integer.
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders '6-number_template.html' template with the provided number.
    """
    return render_template('6-number_template.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders '6-number_odd_or_even.html' template with the provided number and its even/odd status.
    """
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', number=n, is_even=is_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
