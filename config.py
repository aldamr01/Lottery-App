from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = environ.get('DEBUG')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')    
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'