import os

DATABASE_URL = os.environ["DATABASE_URL"]
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False