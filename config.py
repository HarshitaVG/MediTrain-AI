import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-difficult-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
