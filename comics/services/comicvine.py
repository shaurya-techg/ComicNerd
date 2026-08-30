import requests

from django.conf import settings


BASE_URL = "https://comicvine.gamespot.com/api"
TIMEOUT = 10


def make_request(endpoint, params):

    url = f"{BASE_URL}{endpoint}"

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "ComicNerd"
        },
        timeout=TIMEOUT
    )

    response.raise_for_status()

    return response.json()


# Search comics based on a query string
def search_comics(query):

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "query": query,
        "resources": "issue",
    }

    return make_request(
        "/search/",
        params
    )


# Get details of a specific comic issue using its ID
def get_comic_details(issue_id):

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
    }

    return make_request(
        f"/issue/4000-{issue_id}/",
        params
    )


# Get latest comics
def get_latest_comics():

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "sort": "cover_date:desc",
        "limit": 8,
    }

    return make_request(
        "/issues/",
        params
    )


# Get recently updated volumes for the Trending section
def get_trending_comics():

    params = {
        "api_key": settings.COMICVINE_API_KEY,
        "format": "json",
        "sort": "date_last_updated:desc",
        "limit": 8,
    }

    return make_request(
        "/volumes/",
        params
    )