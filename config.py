import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Sets the configuration variables for our Flask app
    Eventually we will use hidden variable items, but for now we'll leave them exposed.
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Decreases unnecessary output in terminal as we use the db