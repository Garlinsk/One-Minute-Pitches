import os
import secrets

class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY= os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get("FLASK_ENV")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex()
    


class ProdConfig(Config):
    DATABASE =""
    POSTGRES_USER =""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI =""
   
    DEBUG = True

class DevConfig(Config):
    FLASK_ENV =os.environ.get("FLASK_ENV")
    DATABASE = os.environ.get("frank")
    POSTGRES_USER =os.environ.get("garlinsk")
    POSTGRES_PASSWORD =os.environ.get("kenya254")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/frank'
        
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
