import os

class Config:
    """Main configurations class"""


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/frank'# os.environ.get("DATABASE_URL")

    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")





class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://garlinsk:kenya254@localhost/frank'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """Configuration class for development stage of the app"""

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://garlinsk:kenya254@localhost/frank'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
    #'test':TestConfig
}