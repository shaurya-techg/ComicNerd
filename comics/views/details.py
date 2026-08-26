from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from reviews.documents import Review
from comics.services.comicvine import get_comic_details

#comic details and reviews waala page.
@login_required
def comic_detail_view(request, issue_id):

    data = get_comic_details(issue_id)

    comic = data.get("results")

    reviews = Review.objects(
        comic_id=str(issue_id)
    ).order_by("-created_at")

    average_rating = 0

    if len(reviews) > 0:

        average_rating = round(
            sum(review.rating for review in reviews) /
            len(reviews),
            1
        )

    return render(
        request,
        "comics/detail.html",
        {
            "comic": comic,
            "reviews": reviews,
            "average_rating": average_rating,
        }
    )
