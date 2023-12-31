#!/usr/bin/python3
"""Starts a flask web application.
"""

from flask import Flask, request,render_template
app = Flask(__name__)

# Define the route from the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'. """
    return "Hello HBNB!"

# Define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'. """
    return "HBNB"

# Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'c' followed by the value of <text>. """
    # Replace underscores with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return "c {}".format(formatted_text)

# Define the route for '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """Displays 'python' followed by the value of <text>.

    Replaces any underscores in <text> with spaces.
    """
    # Replace underscores with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return "python {}".format(formatted_text)

#Define the route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
	"""Displays an HTML page only if<n> is an integer."""
	#Render the template and pass the value of n to the template
	return render_template("5-number.html", n=n)

if __name__ == "__main__":
    # Start the flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
