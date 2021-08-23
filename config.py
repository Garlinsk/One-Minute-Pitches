import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://garlinsk:Kuloba3811@localhost/garlinsk"


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    DEBUG = True

class DevConfig(Config):
        
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
