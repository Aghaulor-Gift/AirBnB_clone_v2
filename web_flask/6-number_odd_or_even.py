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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler for the /number/<n> URL.
    Returns 'n is a number' only if n is an integer.
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the /number_template/<n> URL.
    Renders an HTML page with H1 tag: 'Number: n' inside the tag BODY.
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the /number_odd_or_even/<n> URL.
    Renders an HTML page with H1 tag: 'Number: n is even|odd'
    inside the tag BODY.
    """
    if isinstance(n, int):
        odd_or_even = "even" if n % 2 == 0 else "odd"
        return render_template('odd_or_even.html', number=n,
                               odd_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
