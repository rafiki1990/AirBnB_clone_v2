#!/usr/bin/python3
"""Starts a flask web application.
"""

from flask import Flask
app = Flask(__name__)

#define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB! """
    return "Hello HBNB!"

if __name__=="__main__":
    #Start the flask development server
    #Listen on all (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
