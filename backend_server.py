#!/usr/bin/env python3

from flask import Flask, request, jsonify
app = Flask(__name__)


##	%%	##	%%	##	%%	##	%%	##


@app.route('/', methods = ["GET"])
def index():
	return jsonify({
		"argumentType": "dictionary"
	});

@app.route('/', methods = ["PUT"])
def submit():
	print(request.form)
	# Flask docs just says that this is a dict with 'parsed form data'
	# from POST or PUT requests. But where is it coming from, and
	# what counts as "form data" in this case?
	# Meanwhile, request.args is what I thought this was, the parsed
	# a parsed query string if available.
	# Right now, our plan is to have requests give JSON data inside
	# their body. We should use request.get_json for that case.
	
	# About 'request': https://tedboy.github.io/flask
	# /interface_api.incoming_request_data.html#flask.request
	# It is a proxy, that correctly gets the data for
	# the particular thread accessing it.
	return jsonify({
		"error": "Operation not supported yet!"
	});
	# Please figure out how to give a HTTP error.


##	%%	##	%%	##	%%	##	%%	##


if __name__ == "__main__":
	import backend_database_postgresql as db
	if not db.initialise_database_connection_from_default_config_file():
		print("{}{}{}{}".format(
			"We tried to read database connection settings from ",
			"the config file $HOME/.config/KayaBlog/connection, ",
			"but that didn't go well. Could you check the file? ",
			"If it doesn't exist, please fill it out. Thanks!"
		));
		exit(1);
		
	app.run();
	db.disconnect_database_connection();
