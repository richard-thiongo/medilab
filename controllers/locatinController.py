from flask import jsonify
from services.locations import LocationService


class LocationController:
    def __init__(self):
        self.location_service = LocationService()


    def addLocation(self, request):
        data = request.get_json()
        location = data["location"]
        result = self.location_service.addLocation(location)
        if result:
            return jsonify({"message": "Location added successfully"}), 201
        else:
            return jsonify({"message": "Failed to add location"}), 500
        


    def viewLocations(self):
        result = self.location_service.viewLocations()
        if not result:
            return jsonify({"message": "No locations found"}), 404
        else:
            return jsonify({"locations": result}), 200
        

    def updateLocation(self, request):
        data = request.get_json()
        location = data["location"]
        location_id = data["location_id"]
        result = self.location_service.updateLocation(location_id, location)
        if result:
            return jsonify({"message": "Location updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update location"}), 500