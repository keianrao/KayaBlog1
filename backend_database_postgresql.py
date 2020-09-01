#!/usr/bin/env python3

import psycopg2
import os
import os.path

# Reference for errors:
# https://www.psycopg.org/docs/errors.html
# The most public documentation online are very sparse, be careful.
# For any PostgreSQL error code psycopg2 encounters, it throws
# some sort of DB_API exception. It's rather scattered so, doing
# catch-alls like 'except Exception' isn't the worst strategy..



##	%%	##	%%	##	%%	##	%%	##

_connection = None;



##	%%	##	%%	##	%%	##	%%	##

def initialise_database_connection(host, port, username, password, dbname):
	global _connection
	try:
		_connection = psycopg2.connect(
			dbname = dbname,
			user = username,
			password = password,
			host = host,
			port = port
		);
	except psycopg2.OperationalError as op_err:
		print(op_err);
		return
	# We need to throw something..

	# We have to get a Cursor now.
	# Who should manage the Connection object, actually? Cursor object?
	# Should we maintain the former but return instances of the latter?
	# Or should we maintain all of them, and do all database operations
	# on behalf of the other backend modules?


def initialise_database_connection_from_config_file(filepath):
	"""
	Reads data from the given filepath, then
	initialises a database connection with it.
	"""
	if not os.path.isfile(filepath):
		raise FileNotFoundError("Need file '{}'!".format(filepath));
	with open(filepath) as credentialFile:
		host = credentialFile.readline().strip();
		port = credentialFile.readline().strip();
		username = credentialFile.readline().strip();
		password = credentialFile.readline().strip();
		dbname = credentialFile.readline().strip();
		# Docs don't say what happens near EOF.
		# My experiments suggest that empty lines return '\n', but
		# EOFs return '', the empty string. But that's the minimum.
		# So the code above is safe. 
		# (Although initialise_database_connection below should be
		# ready to see empty strings instead of None)		
		initialise_database_connection(host, port, username, password, dbname);
		
	return True;
	
def initialise_database_connection_from_default_config_file():
	"""
	Reads data from the default config filepath, in $HOME/.config.
	"""
	# If we find no config, we are supposed to create the folders.
	# But if we find no .config folder, the user might be having a
	# non-XDG installation, in which case it'd be good if we could
	# give a prompt asking if it's okay for us to go ahead..
	
	try:
		folderpath = os.environ['HOME'] + "/.config/KayaBlog1";
		# Is it okay if we use Unix-style path separators like this?
		os.makedirs(folderpath, exist_ok=True);
		# Why is this function in os rather than os.path..?
	except KeyError as key_err:
		return False;
	
	filepath = folderpath + "/connection";
	if not os.path.exists(filepath):
		# There was no config file. We won't create one, so return..
		# Later on we should print a message notifying the user.
		# Plus a guide on how a config file looks, of course.
		return False;
	
	return initialise_database_connection_from_config_file(filepath);
	# I don't think our methods here are supposed to use return values,
	# instead if any problems arise they should throw exceptions.
	# Maybe we should follow that?

def disconnect_database_connection():
	if _connection == None:
		return
	_connection.close()
	
