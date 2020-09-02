#!/usr/bin/env python3

# This class connects to the usual database (user config file),
# but it searches for and uses certain test tables instead,
# rather than the tables we normally use for KayaBlog.
# This is by no means a good solution, it'd be much better if
# we had test/development clones of the prod database and
# test our functions + more, directly against them.
#
# But I'm not familliar with how to pull off such a setup
# (multiple databases, copying prod), and my current provider's
# free tier doesn't allow multiple databases.
# So for now I'll make do with this module, which is more like
# a test of *my* knowledge of how to use psycopg's interface.
#
# Note that I connect to the database. I'm not sure what happens
# if we connect twice - later on our code should heave measures 
# for that.

import db

db.initialise_database_connection_from_default_config_file();

def testSelect():
	pass

def testInsert():
	pass

# If our blog later supports deletion through the application,
# we should test for that. Our test tables should also have
# a date column somewhere, so we can sort the results by it.
