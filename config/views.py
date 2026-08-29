from django.shortcuts import render
from django.http import JsonResponse

from comic_collections.documents import ComicCollection
from comics.services.comicvine import (
    get_latest_comics,
    get_trending_comics,
)


def health_view(request):

    return JsonResponse({
        "status": "ok"
    })


def home_view(request):

    latest_comics = []
    trending_comics = []

    # Get trending comics
    try:

        trending_response = get_trending_comics()

        trending_comics = trending_response.get(
            "results",
            []
        )

    except Exception:

        pass

    # Get latest comics
    try:

        latest_response = get_latest_comics()

        latest_comics = latest_response.get(
            "results",
            []
        )

    except Exception:

        pass

    # Get user's collection preview
    collection_preview = []

    if request.user.is_authenticated:

        try:

            collection_preview = ComicCollection.objects(
                user_id=request.user.id
            )[:4]

        except Exception:

            collection_preview = []

    return render(
        request,
        "home.html",
        {
            "collection_preview": collection_preview,
            "trending_comics": trending_comics,
            "latest_comics": latest_comics,
        }
    )