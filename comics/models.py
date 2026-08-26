from django.db import models

# Create your models here.
from mongoengine import *

class Comic(Document):

    comic_id = StringField(
        required=True,
        unique=True
    )

    title = StringField(required=True)

    description = StringField()

    publisher = StringField()

    cover_url = StringField()

    genres = ListField(
        StringField()
    )

    meta = {
        "collection": "comics"
    }