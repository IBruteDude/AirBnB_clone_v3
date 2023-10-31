#!/usr/bin/python3
"""the main server api endpoint"""
from api.v1.views import app_views
from os import getenv
from models import storage
from flask import Flask, make_response, jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' handles 404 error and gives json formatted response '''
    print(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=getenv("HBNB_API_PORT", "5000"),
            threaded=True,
            debug=True)
