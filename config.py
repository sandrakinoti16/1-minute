import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandra:12345@localhost/kinoti'
    SECRET_KEY= os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'sandrakinya6@gmail.com'
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''prod class'''

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}