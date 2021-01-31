
class TerminalView:

    def view_amenity_bicycle_parking(self, bicycle_parking):
        for bicycle_parking in bicycle_parking.bicycle_parkings:
            print(
                    "(",
                    bicycle_parking.type,
                    bicycle_parking.id_osm,
                    bicycle_parking.lat,
                    bicycle_parking.lon,
                    bicycle_parking.amenity,
                    bicycle_parking.name,
                    bicycle_parking.operator,
                    bicycle_parking.covered,
                    bicycle_parking.capacity,
                    bicycle_parking.fee,
                    bicycle_parking.access,
                    bicycle_parking.bicycle_parking,
                    bicycle_parking.maxstay,
                    bicycle_parking.surveillance,
                    ")")