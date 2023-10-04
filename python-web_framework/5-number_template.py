#!/usr/bin/python3
"""
Starts a Flask web application with specific routes, including dynamic routes,
default values, and number_template and number_odd_or_even routes.
"""

from flask import Flask, render_template

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
def c_text(text):
    """
    Displays "C ", followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python ", followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """
    Displays "{} is a number" only if n is an integer.
    Returns 404 if n is not a valid integer.
    """
    try:
        n_int = int(n)
        return "{} is a number".format(n_int)
    except ValueError:
        return "404 Not Found", 404


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """
    Renders '6-number_template.html' template with the provided number.
    Displays if the number is even or odd.
    """
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', number=n, is_even=is_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
