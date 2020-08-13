'''
Auth logic
'''

import logging

from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from src.controller.dto.auth.user import UserDTO
from src.model.user import User

logger = logging.getLogger(__name__)

class Auth:
    '''
    Handles the logic for the authentication and authorization
    '''

    @classmethod
    def authenticate(cls, email, password):
        try:
            logger.debug('Authenticating user')

            # Query user
            user = User.query.filter(User.email == email).one()
            token = cls.issue_token([user.id, user.email])

            if not check_password_hash(user.password, password):
                logger.debug('Invalid password')
                raise Unauthorized('Invalid credentials')

            logger.debug('User %s succesfully authenticated', user.email)
            return UserDTO.complete(user.email, token, user.first_name)
        except MultipleResultsFound:
            logger.error('Multiple accounts for credential, database corrupt')
            raise Unauthorized('Account corrupt, contact technical support')
        except NoResultFound:
            logger.debug('Invalid credentials')
            raise Unauthorized('Invalid credentials')

    @classmethod
    def issue_token(cls, identity):
        logger.debug('Creating authentication token')
        return create_access_token(identity=identity)


class Unauthorized(Exception):
    pass
