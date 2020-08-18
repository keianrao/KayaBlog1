#!/usr/bin/env python3

DATABASE_NAME = "KayaBlog1-dev"

def initialise_database_connection(host, port, username, password):
    connection = connect(
        database = DATABASE_NAME,
        user = username,
        password = password,
        host = "{1}:{2}".format(host, port)
    );
    # Not sure how to proceed from here.
    # I'd like to check if the connection succeeded -
    # The docs do not hint that an exception will be raised..

    # If it succeeded, we then have to get a Cursor, as usual.
    # But I'm not sure how. And, who should manage the Connection
    # object? This module, as a sort of state machine pairing with
    # backend-server.py? Or should we return the Connection object
    # for the latter to keep? But we don't really want database
    # logic in that module.

    # Also, we need to import postgresql's module.


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