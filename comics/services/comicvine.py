import requests

from django.conf import settings


BASE_URL = "https://comicvine.gamespot.com/api"

#for searching comics based on a query string.
def search_comics(query):

    url = f"{BASE_URL}/search/"

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "query": query,
        "resources": "issue",
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ComicNerd"
        }
    )

    return response.json()
#to get details of a specific comic issue using its ID.
def get_comic_details(issue_id):

    url = f"{BASE_URL}/issue/4000-{issue_id}/"

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ComicNerd"
        }
    )

    return response.json()
#to get latest comics.
def get_latest_comics():

    url = f"{BASE_URL}/issues/"

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "sort": "cover_date:desc",
        "limit": 8,
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ComicNerd"
        }
    )

    return response.json()
#trending comics(waise toh comicvine ka koi trending endpoint hai nahi,but ye section dekhne mein accha lagega)
def get_trending_comics():

    url = f"{BASE_URL}/volumes/"

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "sort": "date_last_updated:desc",
        "limit": 8,
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ComicNerd"
        }
    )

    return response.json()