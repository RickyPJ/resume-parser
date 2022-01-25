from os import environ

class Config:
    # SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
