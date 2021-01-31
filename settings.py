# DATABASE NAME
DATABASE_NAME = "osm"

HOST = 'localhost'


# OVERPASS_ENDPOINT_DE
OVERPASS_ENDPOINT_DE = "https://lz4.overpass-api.de/api/interpreter"


# OVERPASS_ENDPOINT_FR
OVERPASS_ENDPOINT_FR = "https://overpass.openstreetmap.fr/api/interpreter"


# BOUND_BOX
BOUND_BOX = {
        "south": 48.7555,
        "west": 2.3110,
        "north": 48.7830,
        "east": 2.31969}


## NODES

# AMENITIES (bicycle parking for test)
AMENITIES = """
        "bicycle_parking"
        """


# AMENITIES = """
#         "bar|bbq|biergarten|cafe|drinking_water|fast_food|food_court|ice_cream|pub|restaurant|bicycle_parking|bicycle_repair_station|bicycle_rental|atm|bank|bureau_de_change|hospital|pharmacy|bench|internet_cafe|police|shelter|shower|toilets"
#         """

SHOPS = """
        "bakery|cheese|butcher|deli|greengrocer|ice_cream|pasta|pastry|department_store|general|kiosk|mall|supermarket|bicycle|outdoor|sports|laundry"
        """

PLACES = """
        "country|state|place|region|province|district|county|municipality|city|borough|suburb|quarter|neighbourhood|city_block|plot|town|village|hamlet|solated_dwelling|farm|allotments"
        """

TOURISMS = """
        "apartment|attraction|camp_site|chalet|guest_house|hostel|hotel|information|picnic_site|viewpoint"
        """

HISTORICS = """
        "aqueduct|archaeological_site|battlefield|bomb_crater|boundary_stone|building|castle|castle_wall|charcoal_pile|church|city_gate|citywalls|farm|fort|manor|memorial|milestone|monastery|monument|ruins|rune_stone|ship|tank|tomb"
        """

LEISURES = """
        "beach_resort|firepit|bird_hide|fishing|marina|nature_reserve|park|picnic_table|swimming_area|swimming_pool"
        """