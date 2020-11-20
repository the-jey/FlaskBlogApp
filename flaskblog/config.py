import os

class Config:

    # SECRET_KEY = '5363738939300303038EDEEBVCGEJ93939303'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # MAIL_USERNAME = 'jerem.palmieri.1998@gmail.com'
    # MAIL_PASSWORD = 'uvolmcsdjzyfhqnx'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # uvolmcsdjzyfhqnx
