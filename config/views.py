from django.shortcuts import render

from comic_collections.documents import ComicCollection
from comics.services.comicvine import (get_latest_comics,get_trending_comics)

latest_comics = []
trending_comics = []

try:

    trending_response = get_trending_comics()

    trending_comics = trending_response.get(
        "results",
        []
    )

except Exception:

    pass

try:

    latest_response = get_latest_comics()

    latest_comics = latest_response.get(
        "results",
        []
    )

except Exception:

    pass


def home_view(request):

    collection_preview = []

    if request.user.is_authenticated:

        collection_preview = ComicCollection.objects(
            user_id=request.user.id
        )[:4]

    return render(
        request,
        "home.html",
        {
            "collection_preview": collection_preview,
            "trending_comics": trending_comics,
            "latest_comics": latest_comics,
        }
    )