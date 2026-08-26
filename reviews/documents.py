from mongoengine import (
    Document,
    IntField,
    StringField,
    DateTimeField,
)

from datetime import datetime


class Review(Document):

    user_id = IntField(required=True)

    username = StringField(required=True)

    comic_id = StringField(required=True)

    comic_title = StringField(required=True)

    rating = IntField(required=True)

    review_text = StringField()

    created_at = DateTimeField(
        default=datetime.utcnow
    )