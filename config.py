import os

class Config:
    """
    General configuration parent class
    """
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    

class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    # DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:123456@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
}