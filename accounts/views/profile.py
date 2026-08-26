from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from comic_collections.documents import ComicCollection
from reviews.documents import Review


@login_required
def profile_view(request):

    collection_count = ComicCollection.objects(
        user_id=request.user.id
    ).count()

    review_count = Review.objects(
        user_id=request.user.id
    ).count()

    recent_collection = ComicCollection.objects(
        user_id=request.user.id
    ).order_by("-added_at")[:4]

    recent_reviews = Review.objects(
        user_id=request.user.id
    ).order_by("-created_at")[:4]

    return render(
        request,
        "account/profile.html",
        {
            "collection_count": collection_count,
            "review_count": review_count,
            "recent_collection": recent_collection,
            "recent_reviews": recent_reviews,
        }
    )
    