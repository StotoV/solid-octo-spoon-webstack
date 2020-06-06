'''
Auth controller, all endspoints for authentication and authorization
'''

import logging
import json

from flask_api import status
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from src.service.auth import Auth, Unauthorized

authBlueprint = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)


@authBlueprint.route('/login', methods=['POST'])
def login():
    logger.debug('Request: /login')
    email = request.form['email']
    password = request.form['password']

    try:
        response = Auth().authenticate(email, password)
        return response.serialize(), status.HTTP_200_OK
    except Unauthorized as e:
        return json.dumps(str(e)), status.HTTP_401_UNAUTHORIZED

@authBlueprint.route('/hello')
@jwt_required
def hello():
    logger.debug('Request: /hello')
    return 'Hello world!'
