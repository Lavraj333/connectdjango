import requests
from django.conf import settings

TMDB_URL = "https://api.themoviedb.org/3/search/person"

def get_tmdb_profile(name):

    params = {
        "query": name,
        "api_key": settings.TMDB_API_KEY
    }

    try:
        response = requests.get(TMDB_URL, params=params)

        data = response.json()

        # check if results exist
        if "results" in data and len(data["results"]) > 0:
            return data["results"][0].get("profile_path")

        return None

    except Exception as e:
        print("TMDB error:", e)
        return None