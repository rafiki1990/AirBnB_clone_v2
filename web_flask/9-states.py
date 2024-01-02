#!/usr/bin/python3
""" Starts a Flash web application. """

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# creates an instance of the Flask class and assigns it to the variable app
app = Flask(__name__)

# Teardown app context to remove the
#       current SQLAlchemy session after each request
@app.teardown_app_context
def teardown_app_context(exception):
        """Remove the current SQLAlchemy session."""
        storage.close()

# Define the route for '/states'
@app.route('/states', strict_slashes=False)
def states():
	""" Displays an HTML page with a list of all states.

	States are sorted by name.
	"""
	# Fetch all state objects from the storage (FileStorage or DBStorage)
	states = storage.all("State")

	# Render the "9-states.html" template and pass
	#	the list of status as the variable 'state'
	return render_template("9-states.html", states=states)

# Define the route for '/states/<id>'
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
	"""Displays an HTML page with info about <id>, if it exists."""
	# Loop though all state objects in the storage
	#	(either FileStorage or DBStorage)
	for state in storage.all("State").values():
		# Check if the current state object's id matches the requested <id>
		if state.id == id:
			# If a matching state is found,
			#   render the template and pass the state object to the template 
			return render_template("9-state.html", state=state)
	# If no matching state is found,
	#	render the template without passing any state object
	return render_template("9-state.html")


if __name__=="__main__":
        # Start the Flash development server
        # Listen on all available network interfaces (0.0.0.0) and port 5000
        app.run(host='0.0.0.0', port=5000)	
