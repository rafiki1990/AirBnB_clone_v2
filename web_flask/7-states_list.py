#!/usr/bin/python3
""" Starts a Flash web application. """

from flash import Flash,render_template
from models import storage
from models.state import state
from sqlalchemy.orm import scope_session, sessionmaker

# Creates an instance of the Flask class and assigns it to the variable app
app = Flask(__name__)


# Teardown app context to remove the
#   current SQLAlchemy session after each request
@app.teardown_appcontext
def teardown(exception):
	"""Remove the current SQLAlchemy session. """
	storage.close()


# Define the route for '/states_list'
@app.route("/states_list", strict_slashes=False)
def states_list():
	"""Displays an HTML page with a list of all state objects in DBStorage.

	States are sorted by name.
	"""
	# Fetch all States objects from the DBStorage and sort them by name (A->Z)
	states = sorted(storage.all(State).value(), key=lambda s: s.name)

	# Render the template and pass the list of states to the template
	return render_template("7-states_list.html", states=states)


if __name__=="__main__":
	# Start the Flask development server
	# Listin on all available network interfaces (0.0.0.0) and port 5000
	app.run(host='0.0.0.0', port=5000)
