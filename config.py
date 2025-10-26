from os import path, environ, getenv

BASE_DIR =path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = 'key'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'pms'
    ASSETS_DEBUG = True

    # MAIL_SERVER= getenv('MAIL_SERVER')
    # MAIL_PORT = getenv('MAIL_PORT')
    # MAIL_UserNAME = getenv('MAIL_UserNAME')
    # MAIL_PASSWORD= getenv('MAIL_PASSWORD')
    # MAIL_USE_TLS = getenv('MAIL_USE_TLS')
    # MAIL_USE_SSL = getenv('MAIL_USE_SSL')
