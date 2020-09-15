#!/usr/bin/env python3

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
app = Flask(__name__)


##	%%	##	%%	##	%%	##	%%	##


@app.route('/', methods = ["GET"])
def index():
	return jsonify({
		"argumentType": "dictionary"
	});

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

	response = jsonify({
		"error": "Operation not supported yet!"
	});
	response.status_code = 500;
	return response;


##	%%	##	%%	##	%%	##	%%	##


if __name__ == "__main__":
	import backend_database_postgresql as db
	if not db.initialise_database_connection_from_default_config_file():
		print("{}{}{}{}".format(
			"We tried to read database connection settings from ",
			"the config file $HOME/.config/KayaBlog1/connection, ",
			"but that didn't go well. Could you check the file? ",
			"If it doesn't exist, please fill it out. Thanks!"
		));
		exit(1);

	app.run();
	db.disconnect_database_connection();
