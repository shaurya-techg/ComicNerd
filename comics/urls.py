from django.urls import path

from .views import (
    search_view,
    comic_detail_view
)

urlpatterns = [
    path("", search_view, name="comic_search"),

    path(
        "<int:issue_id>/",
        comic_detail_view,
        name="comic_detail"
    ),
]