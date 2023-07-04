import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

