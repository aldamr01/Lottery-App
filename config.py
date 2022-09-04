from os import environ
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    DEBUG = environ.get('DEBUG')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')    
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    WTF_CSRF_FIELD_NAME = 'csrf_token'
    WTF_CSRF_ENABLED = True
    SESSION_COOKIE_DOMAIN = False
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    
class GeneralConfig:
    APP_NAME = environ.get('APP_NAME')