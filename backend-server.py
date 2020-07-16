#!/usr/bin/env python3

from flask import Flask, request, jsonify
app = Flask(__name__)

# Read credentials
import os.path
if not os.path.isfile('database-credentials.cfg'):
    raise FileNotFoundError("Need file 'database-credentials.cfg'!");
with open('database-credentials.cfg') as credentialFile:
    username = credentialFile.readline();
    password = credentialFile.readline();

##  %%  ##  %%  ##  %%  ##  %%  ##

@app.route('/', methods = ["GET"])
def index():
    return jsonify({
        "argumentType": "dictionary"
    });

@app.route('/', methods = ["PUT"])
def submit():
    print(request.form)
    # request.form is a dictionary that contains POST data - key-value pairs.
    # It's more appropriate for a route with method 'POST' rather than 'PUT',
    # but we're not going to use POST data in our app actually.
    # We'll continue using PUT, and accept JSON data through request.json.
    # ...Also, by sheer force of miracle, we can access a request object
    # despite having no arguments in our function. Is this request object
    # we're using specific to this entire Python process, and a new instance of
    # Python is run everytime a request comes in?
    return jsonify({
        "error": "Operation not supported yet!"
    });
    # Please figure out how to give a HTTP error.

##  %%  ##  %%  ##  %%  ##  %%  ##

if __name__ == "__main__":
    app.run()
