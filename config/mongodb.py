import os

from mongoengine import connect


def initialize_db():

    mongo_uri = os.getenv("MONGODB_URI")
    mongo_db = os.getenv("MONGODB_DB")

    if not mongo_uri:
        raise RuntimeError("MONGODB_URI is not configured.")

    if not mongo_db:
        raise RuntimeError("MONGODB_DB is not configured.")

    connect(
        db=mongo_db,
        host=mongo_uri,
    )