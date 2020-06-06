'''
The different environments
'''

import os
import logging

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

logger = logging.getLogger(__name__)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bycript = Bcrypt()


def create_app(config_name):
    '''
    Create the app with the correct config
    '''

    logger.debug('Creating Flask app')
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    logger.debug('Config created with the following parameters: %s',
                 app.config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bycript.init_app(app)
    logger.debug('Helpers initialized')

    # Import models
    from src.model import user

    return app


class Config:
    '''
    App config
    '''

    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    JWT_SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig,
                      test=TestingConfig,
                      prod=ProductionConfig)
