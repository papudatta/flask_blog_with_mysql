import os

SECRET_KEY = 'SuperSecret'
DEBUG = True

DB_USER = 'flaskuser'
DB_PASSWORD = 'flaskpass'
DB_BLOG = 'flaskblog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USER,
                                              DB_PASSWORD,
                                              DB_HOST,
                                              DB_BLOG)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/Users/paps/Desktop/flask/blog_with_flask/static/images/'
UPLOADED_IMAGES_URL = '/static/images/'
