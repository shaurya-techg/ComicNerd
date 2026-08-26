from mongoengine import (
    Document,
    StringField,
    IntField,
    DateTimeField
)

from datetime import datetime


class ComicCollection(Document):

    user_id = IntField(required=True)

    comic_id = IntField(required=True)

    comic_title = StringField(required=True)

    cover_url = StringField()

    added_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "comic_collections"
    }