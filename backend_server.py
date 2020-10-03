#!/usr/bin/env python3

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
app = Flask(__name__)

from backend_errors import \
	ContentTypeNotJsonException, NotWellFormedJsonException, \
	WrongArgumentTypeException, EntityNotFoundException



##	%%	##	%%	##	%%	##	%%	##

@app.route('/', methods = ["GET"])
def index():
	# If no arguments, probably return all entries.
	# But maybe at this same endpoint, if arguments are given,
	# search for and return specific entries.
	# That needs to be supported by the database module,
	# for now we should just aim for it returning all entries.
	
	#input_data = get_json();
	
	return _create_http_jsonify_response(
		200, 
		list(map(lambda l: l._asdict(), db.get_blogpost_listings()))
	);


@app.route('/read', methods = ["GET"])
def read():
	input_data = _get_json();
	
	if "blogpostID" not in input_data:
		return _create_http_jsonify_response(400, {
			"errorMessage": "A blogpost ID is needed.",
			"missingFields": "blogpostID"
		});
	
	# Otherwise, fetch from database
	blogpost_id = input_data["blogpostID"];
	try:
		blogpost = db.get_blogpost_by_id(blogpost_id);
		return _create_http_jsonify_response(200, {
			"title": blogpost.title,
			"authorUsername": blogpost.authorUsername,
			"submissionDate": blogpost.submissionDate,
			"tags": blogpost.tags,
			"contents": blogpost.contents
		});
	except EntityNotFoundException:
		return _create_http_jsonify_response(400, {
			"errorMessage": "No blogpost was found with that ID.",
			"id": blogpost_id
		});
	except WrongArgumentTypeException:
		return _create_http_jsonify_response(400, {
			"errorMessage": "The blogpost ID was of an invalid format.",
			"id": blogpost_id
		});



@app.route('/', methods = ["POST"])
def submit():
	input_data = _get_json();

	# Flask parses the JSON into a Python dictionary, so use it as such.
	# Now. See if they provided all the fields we need.
	expected_keys = ["title", "tags", "contents", "username"];
	missing_keys = [key for key in expected_keys if key not in input_data];
	if missing_keys:
		return _create_http_jsonify_response(400, {
			"errorMessage": "Some fields are missing",
			"missingFields": missing_keys
		});

	# Okay, then double-check all the fields, see if they're valid.
	# Maybe sanitise them?
	# Otherwise, send it to the database module.

	raise NotImplementedError;
	
	
@app.errorhandler(NotImplementedError)
def response_for_not_implemented_error(e):
	return _create_http_jsonify_response(501, {
		"errorMessage": "Operation not supported yet!"
	});
	
	
@app.errorhandler(ContentTypeNotJsonException)
def response_for_content_type_not_json_exception(e):
	return _create_http_jsonify_response(400, {
		"errorMessage": \
			"Request mimetype is not 'application/json'!" \
	        " This API endpoint only supports JSON requests."
	});
	
	
@app.errorhandler(NotWellFormedJsonException)
def response_for_not_well_formed_json_exception(e):
	return _create_http_jsonify_response(400, {
		"errorMessage": "Request data is not well-formed JSON!"
	});



##	%%	##	%%	##	%%	##	%%	##

def _get_json():
	if not request.is_json:
		raise ContentTypeNotJsonException;
	try:
		return request.get_json();
	except BadRequest:
		raise NotWellFormedJsonException;
		
		
		
def _create_http_jsonify_response(http_code, dictionary):
	response = jsonify(dictionary);
	response.code = http_code;
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
	# app.run() has to be called down here, after all else has been declared.
	db.disconnect_database_connection();
