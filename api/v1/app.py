#!/usr/bin/python3
"""the main server api endpoint"""
from flask import Flask, redirect, Request, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views 

app = Flask(__name__)

@app.teardown_appcontext
def app_teardown():
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=getenv("HBNB_API_PORT", "5000"), threaded=True)

"""

register the blueprint app_views to your Flask instance app
declare a method to handle @app.teardown_appcontext that calls storage.close()
inside if __name__ == "__main__":, run your Flask server (variable app) with:
host = environment variable HBNB_API_HOST or 0.0.0.0 if not defined
port = environment variable HBNB_API_PORT or 5000 if not defined
threaded=True
Create a folder views inside v1:
    create a file __init__.py:
        import Blueprint from flask doc
        create a variable app_views which is an instance of Blueprint (url prefix must be /api/v1)
        wildcard import of everything in the package api.v1.views.index => PEP8 will complain about it, don’t worry, it’s normal and this file (v1/views/__init__.py) won’t be check.
    create a file index.py
        import app_views from api.v1.views
        create a route /status on the object app_views that returns a JSON: "status": "OK" (see example)
"""
