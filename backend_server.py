#!/usr/bin/env python3

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
app = Flask(__name__)

from backend_errors import ContentTypeNotJsonException, NotWellFormedJsonException



##	%%	##	%%	##	%%	##	%%	##

@app.route('/', methods = ["GET"])
def index():
	# If no arguments, probably return all entries.
	# But maybe at this same endpoint, if arguments are given,
	# search for and return specific entries.
	# That needs to be supported by the database module,
	# for now we should just aim for it returning all entries.
	
	#input_data = get_json();
	
	raise NotImplementedError;



@app.route('/read', methods = ["GET"])
def read():
	#input_data = _get_json();
	
	# Find blogpost ID in query parameters

	# If none, bjork

	# Otherwise, fetch from database

	# Convert to JSON

	# Send back

	raise NotImplementedError;



@app.route('/', methods = ["POST"])
def submit():
	input_data = _get_json();

	# Flask parses the JSON into a Python dictionary, so use it as such.
	# Now. See if they provided all the fields we need.
	expected_keys = ["title", "tags", "contents", "username"];
	missing_keys = [key for key in expected_keys if key not in input_data];
	if missing_keys:
		response = jsonify({
			"errorMessage": "Some fields are missing",
			"missingFields": missing_keys
		});
		response.status_code = 400;
		return response;

	# Okay, then double-check all the fields, see if they're valid.
	# Maybe sanitise them?
	# Otherwise, send it to the database module.

	raise NotImplementedError;
	
	
	
@app.errorhandler(NotImplementedError)
def response_for_not_implemented_error(e):
	response = jsonify({
		"errorMessage": "Operation not supported yet!"
	});
	response.code = 501;
	return response;
	
	
	
@app.errorhandler(ContentTypeNotJsonException)
def response_for_content_type_not_json_exception(e):
	response = jsonify({
		"errorMessage": \
			"Request mimetype is not 'application/json'!" \
	        " This API endpoint only supports JSON requests."
	});
	response.code = 400;
	return response;
	
	
	
@app.errorhandler(NotWellFormedJsonException)
def response_for_not_well_formed_json_exception(e):
	response = jsonify({
		"errorMessage": "Request data is not well-formed JSON!"
	});
	response.code = 400;
	return response;



##	%%	##	%%	##	%%	##	%%	##
	
def _get_json():
	if not request.is_json:
		raise ContentTypeNotJsonException;
	try:
		return request.get_json();
	except BadRequest:
		raise NotWellFormedJsonException;
		
		
		
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
	# app.run() has to be called down here, after all else has been declared.
	db.disconnect_database_connection();
