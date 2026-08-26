from django.db import models

# Create your models here.
from mongoengine import *

class Review(Document):

    user_id = StringField(required=True)

    comic_id = StringField(required=True)

    rating = IntField(
        min_value=1,
        max_value=5
    )

    review_text = StringField()

    meta = {
        "collection": "reviews"
    }