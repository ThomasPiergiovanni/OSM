"""Overpass module. For connection wiyt Overpass API (OSM)
"""
import requests
import json

from settings import (
        OVERPASS_ENDPOINT_DE,
        OVERPASS_ENDPOINT_FR,
        BOUND_BOX,
        AMENITIES,
        SHOPS,
        PLACES,
        TOURISMS,
        HISTORICS,
        LEISURES
        )


class Overpass:
    """Overpass API connection
    """
    def __init__(self):
        """
        """
        self.response = None

    def request_bicycle_parking_by_postal_codes(self, postal_code):
        """
        """
        overpass_query = """
            [out:json];
            area["postal_code"=""" + postal_code + """][admin_level=8];
            node["amenity"~""" + AMENITIES + """](area)->.amenities;
            (
                .amenities;
            )->.all;
            (.all;);
            out geom;
            """
        response = requests.get(
                OVERPASS_ENDPOINT_DE, params={'data': overpass_query})
        self.response = response.json()

    # def request_all_places_by_postal_codes(self, postal_code):
    #     """
    #     """
    #     overpass_query = """
    #         [out:json];
    #         area["postal_code"=""" + postal_code + """][admin_level=8];
    #         node["amenity"~""" + AMENITIES + """](area)->.amenities;
    #         node["shop"~""" + SHOPS + """](area)->.shops;
    #         node["places"~""" + PLACES + """](area)->.places;
    #         node["tourisms"~""" + TOURISMS + """](area)->.tourisms;
    #         node["histrorics"~""" + HISTORICS + """](area)->.histrorics;
    #         node["leisures"~""" + LEISURES + """](area)->.leisures;
    #         (
    #             .amenities;
    #             .shops;
    #             .places;
    #             .tourisms;
    #             .histrorics;
    #             .leisures;
    #         )->.all;
    #         (.all;);
    #         out geom;
    #         """
    #     response = requests.get(
    #             OVERPASS_ENDPOINT_FR, params={'data': overpass_query})
    #     self.response = response.json()