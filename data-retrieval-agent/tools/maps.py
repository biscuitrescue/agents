from typing import Dict, Any
import googlemaps
import os

api_key = os.environ.get("GOOGLE_CLOUD_SECRET")
gmaps: googlemaps.Client = googlemaps.Client(key=api_key)


def get_route(origin: str, destination: str, api_key: str) -> Dict[str, Any]:
    try:
        gmaps = googlemaps.Client(key=api_key)
        directions = gmaps.directions(  # type: ignore[attr-defined]
            origin,
            destination,
            mode="driving",
            departure_time="now",
            traffic_model="best_guess",
        )
        return directions[0] if directions else {"error": "No route found"}
    except Exception as e:
        return {"error": f"Google Maps API error: {e}"}
