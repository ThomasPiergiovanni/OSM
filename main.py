from controller.apiclient.overpass import Overpass
from controller.database.connection_manager import ConnectionManager
from model.bicycle_parking import BicycleParking
from view.terminal_view import TerminalView



def overpass_connection():
    overpass = Overpass()
    overpass.request_bicycle_parking_by_postal_codes("92150")
    return overpass

def instanciate_bicycle_parking(overpass):
    bicycle_parking = BicycleParking()
    bicycle_parking.create_amenity_bicycle_parking(overpass)
    return bicycle_parking

def display_bicycle_parking(bicycle_parking):
    terminal_view = TerminalView()
    terminal_view.view_amenity_bicycle_parking(
            bicycle_parking)

def set_database():
    connection_manager = ConnectionManager()

if __name__ == '__main__':
    # overpass = overpass_connection()
    # bicycle_parking = instanciate_bicycle_parking(overpass)
    # display_bicycle_parking(bicycle_parking)
    set_database()
