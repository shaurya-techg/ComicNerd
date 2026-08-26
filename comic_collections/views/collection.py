from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from comic_collections.documents import ComicCollection


@login_required
def my_collection_view(request):

    query = request.GET.get("q", "").strip()

    comics = ComicCollection.objects(
        user_id=request.user.id
    )

    if query:

        comics = comics.filter(
            comic_title__icontains=query
        )

    return render(
        request,
        "comic_collections/my_collection.html",
        {
            "comics": comics,
            "query": query,
        }
    )


@login_required
def add_to_collection_view(request):

    comic_id = request.GET.get("comic_id")

    title = request.GET.get("title")

    cover_url = request.GET.get("cover_url")

    existing = ComicCollection.objects(
        user_id=request.user.id,
        comic_id=comic_id
    ).first()

    if not existing:

        ComicCollection(
            user_id=request.user.id,
            comic_id=comic_id,
            comic_title=title,
            cover_url=cover_url,
        ).save()

    return redirect("my_collection")


@login_required
def remove_from_collection_view(request, comic_id):

    ComicCollection.objects(
        user_id=request.user.id,
        comic_id=comic_id
    ).delete()

    return redirect("my_collection")