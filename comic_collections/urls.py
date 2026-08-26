from django.urls import path

from .views import (
    my_collection_view,
    add_to_collection_view,
    remove_from_collection_view,
)

urlpatterns = [
    path(
        "",
        my_collection_view,
        name="my_collection",
    ),

    path(
        "add/",
        add_to_collection_view,
        name="add_to_collection",
    ),
    path(
        "remove/<int:comic_id>/",
        remove_from_collection_view,
        name="remove_from_collection",),
]