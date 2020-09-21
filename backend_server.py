#!/usr/bin/env python3

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
app = Flask(__name__)


##	%%	##	%%	##	%%	##	%%	##


@app.route('/', methods = ["GET"])
def index():
	# If no arguments, probably return all entries.
	# But maybe at this same endpoint, if arguments are given,
	# search for and return specific entries.
	# That needs to be supported by the database module,
	# for now we should just aim for it returning all entries.

	response = jsonify({
		"error": "Operation not supported yet!"
	});
	response.status_code = 501;
	return response;


@app.route('/read', methods = ["GET"])
def read():
    # Find blogpost ID in query parameters

    # If none, bjork

    # Otherwise, fetch from database

    # Convert to JSON

    # Send back

	response = jsonify({
		"error": "Operation not supported yet!"
	});
	response.status_code = 501;
	return response;


@app.route('/', methods = ["POST"])
def submit():
	if not request.is_json:
		response = jsonify({
			"error": "Input data must be in the form of JSON!" \
				" Check that the request mimetype is 'application/json'."
		});
		response.status_code = 400;
		return response;

	try:
		input_data = request.get_json();
	except BadRequest:
		response = jsonify({
			"error": "Input data must be in the form of JSON!" \
				" Check that the data in the request is well-formed JSON."
		});
		response.status_code = 400;
		return response;

	# Note: We can break off the following code to a new function.

	# Okay, everything went okay.
	# Flask parses the JSON into a Python dictionary, so use it as such.
	# Now. See if they provided all the fields we need.
	expected_keys = ["title", "tags", "contents", "username"]
	missing_keys = [key for key in expected_keys if key not in input_data]
	if missing_keys:
		response = jsonify({
			"error": "Some fields are missing",
			"missingFields": missing_keys
		});
		response.status_code = 400;
		return response;

	# Do double-check if they're empty.

	# If not, then we have values for everything.
	# Perhaps we should sanitise the values first? Somehow?
	# Otherwise, send it off to the database module.

	response = jsonify({
		"error": "Operation not supported yet!"
	});
	response.status_code = 501;
	return response;


##	%%	##	%%	##	%%	##	%%	##


if __name__ == "__main__":
	import backend_database_postgresql as db
	if not db.initialise_database_connection_from_default_config_file():
		print(
			"We tried to read database connection settings from "
			"the config file $HOME/.config/KayaBlog1/connection, "
			"but that didn't go well. Could you check the file? "
			"If it doesn't exist, please fill it out. Thanks!"
		);
		exit(1);

	app.run();
	db.disconnect_database_connection();
