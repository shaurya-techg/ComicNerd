from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from reviews.documents import Review


@login_required
def add_review_view(request):

    if request.method == "POST":

        comic_id = request.POST.get("comic_id")

        Review(
            user_id=request.user.id,
            username=request.user.username,
            comic_id=comic_id,
            comic_title=request.POST.get("comic_title"),
            rating=int(request.POST.get("rating")),
            review_text=request.POST.get("review_text"),
        ).save()

        # Return to the same comic detail page
        return redirect("comic_detail", issue_id=comic_id)

    return redirect("home")


def get_reviews_for_comic(comic_id):

    return Review.objects(
        comic_id=str(comic_id)
    ).order_by("-created_at")