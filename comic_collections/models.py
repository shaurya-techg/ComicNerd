from django.db import models

# Create your models here.
from mongoengine import *

class Collection(Document):

    user_id = StringField(required=True)

    comic_id = StringField(required=True)

    status = StringField(
        choices=[
            "reading",
            "completed",
            "wishlist"
        ]
    )

    meta = {
        "collection": "collections"
    }