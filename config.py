import os

ADMIN_PASSWORD = "jimmy"
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = "sqliteext://{}".format(os.path.join(APP_DIR, "blog.db"))
DEBUG = True
SECRET_KEY = "rustle"
SITE_WIDTH = 800