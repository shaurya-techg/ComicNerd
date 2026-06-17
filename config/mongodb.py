from mongoengine import connect
import os

def initialize_db():
    connect(
        db=os.getenv("MONGODB_DB"),
        host=os.getenv("MONGODB_HOST"),
        port=int(os.getenv("MONGODB_PORT"))
    )