#!/usr/bin/python3
"""index module scripts"""


from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """returns a JSON: "status": "OK" """
    return jsonify(status='OK')


@app_views.route('/status')
def api_stat():
    """retrieves the number of each objects by type"""
    return jsonify({
                    "amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")
                  })
