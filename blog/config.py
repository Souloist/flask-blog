import os

ADMIN_PASSWORD = "jimmy"
APP_DIR = os.path.dirname(os.path.realpath(__file__))
SQLALCHEMY_DATABASE_URI = (
    "sqlite:///{}".format(os.path.join(APP_DIR,"blog.db"))
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
SECRET_KEY = "rustle"
SITE_WIDTH = 800
