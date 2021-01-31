"""Bicycle Parking  module
"""


class BicycleParking:
    """ BicycleParking class
    """

    bicycle_parkings = []

    def __init__(self):
        self.type = None
        self.id_osm = None
        self.lat = None
        self.lon = None
        self.amenity = None
        self.name = None
        self.operator = None
        self.covered = None
        self.capacity = None
        self.fee = None
        self.access = None
        self.bicycle_parking = None
        self.maxstay = None
        self.surveillance = None
    
    @classmethod
    def create_amenity_bicycle_parking(cls, overpass):
        """
        """
        elements = overpass.response["elements"]
        for element in elements:
            if "amenity" in element["tags"].keys():
                if element["tags"]["amenity"] == "bicycle_parking":
                    bicycle_parking = BicycleParking()
                    bicycle_parking.amenity = element["tags"]["amenity"]
                    if "type" in element.keys():
                        bicycle_parking.type = element["type"]
                    if "id" in element.keys():
                        bicycle_parking.id_osm = element["id"]
                    if "lat" in element.keys():
                        bicycle_parking.lat = element["lat"]
                    if "lon" in element.keys():
                        bicycle_parking.lon = element["lon"]
                    if "name" in element["tags"].keys():
                        bicycle_parking.name = element["tags"]["name"]
                    if "operator" in element["tags"].keys():
                        bicycle_parking.operator = element["tags"]["operator"]
                    if "covered" in element["tags"].keys():
                        bicycle_parking.covered = element["tags"]["covered"]
                    if "capacity" in element["tags"].keys():
                        bicycle_parking.capacity = element["tags"]["capacity"]
                    if "fee" in element["tags"].keys():
                        bicycle_parking.fee = element["tags"]["fee"]
                    if "access" in element["tags"].keys():
                        bicycle_parking.access = element["tags"]["access"]
                    if "bicycle_parking" in element["tags"].keys():
                        bicycle_parking.bicycle_parking = (
                                element["tags"]["bicycle_parking"])
                    if "maxstay" in element["tags"].keys():
                        bicycle_parking.maxstay = element["tags"]["maxstay"]
                    if "surveillance" in element["tags"].keys():
                        bicycle_parking.surveillance = (
                                element["tags"]["surveillance"])
                    cls.bicycle_parkings.append(bicycle_parking)