from django.urls import path

from .views import add_review_view

urlpatterns = [

    path(
        "add/",
        add_review_view,
        name="add_review"
    ),

]