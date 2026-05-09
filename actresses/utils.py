import requests
from django.conf import settings

TMDB_URL = "https://api.themoviedb.org/3/search/person"
TMDB_BASE = "https://image.tmdb.org/t/p/h632"

def get_tmdb_profile(name):
    params = {
        "query": name,
        "api_key": settings.TMDB_API_KEY
    }
    try:
        response = requests.get(TMDB_URL, params=params)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            path = data["results"][0].get("profile_path")
            if path:
                return f"{TMDB_BASE}{path}"  # ← return full URL now
        return None
    except Exception as e:
        print("TMDB error:", e)
        return None