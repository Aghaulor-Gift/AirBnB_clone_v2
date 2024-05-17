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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
