import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://db:db:5432/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='dev'