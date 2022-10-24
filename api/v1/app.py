#!/usr/bin/python3
"""
API application file
"""


from os import getenv
from models import storage
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api.vi.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app,resourses={"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_appcontext(self):
    """Close storage session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """returns a JSON-formatted 404 status code response"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=getenv('HBNB_API_PORT', 5000),
        threaded=True
    )
