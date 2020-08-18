#!/usr/bin/env python3

import psycopg2

_DATABASE_NAME = "KayaBlog1-dev"


# Reference for errors:
# https://www.psycopg.org/docs/errors.html
# The most public documentation online are very sparse, be careful.
# For any PostgreSQL error code psycopg2 encounters, it throws
# some sort of DB_API exception. It's rather scattered so, doing
# catch-alls like 'except Exception' isn't the worst strategy..


##  %%  ##  %%  ##  %%  ##  %%  ##


def initialise_database_connection(host, port, username, password):
    global _connection
    try:
        _connection = psycopg2.connect(
            dbname = _DATABASE_NAME,
            user = username,
            password = password,
            host = host,
            port = port
        );
    except psycopg2.OperationalError as op_err:
        _connection = None

    # We have to get a Cursor now.
    # Who should manage the Connection object, actually? Cursor object?
    # Should we maintain the former but return instances of the latter?
    # Or should we maintain all of them, and do all database operations
    # on behalf of the other backend modules?


def initialise_database_connection_from_config_file(filepath):
    import os.path
    if not os.path.isfile(filepath):
        raise FileNotFoundError("Need file '{}'!".format(filepath));
    with open(filepath) as credentialFile:
        host = credentialFile.readline().strip();
        port = credentialFile.readline().strip();
        username = credentialFile.readline().strip();
        password = credentialFile.readline().strip();
        initialise_database_connection(host, port, username, password);
