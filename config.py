import os


class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY= os.environ.get('SECRET_KEY')
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/frank'


    SECRET_KEY = "try harder" #os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    """Production configuration class that inherits from the main configurations class"""

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/frank'
   # os.environ.get("DATABASE_URL")
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
    DEBUG = True

class DevConfig(Config):

    """Configuration class for development stage of the app"""
    DEBUG = True

    # FLASK_ENV =os.environ.get("FLASK_ENV")
    # DATABASE = os.environ.get("frank")
    # POSTGRES_USER =os.environ.get("garlinsk")
    # POSTGRES_PASSWORD =os.environ.get("kenya254")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/frank'
        
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
