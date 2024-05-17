#!/usr/bin/python3
""" Script that starts a Flask web application
listening on 0.0.0.0, port 5000 and displays 'Hello HBNB!' on the homepage.
/hbnb: display “HBNB”
"""

from flask import Flask
app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL. Returns 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route handler for the root URL. Returns "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the /c/<text> URL.
    Returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route handler for the /python/<text> URL.
    Returns 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces.
    The default value for text is 'is cool'.
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
