'''
User DTO
'''

from ..dto import DTO

class UserDTO(DTO):
    def __init__(self, email, token):
        self.email = email
        self.token = token

    @classmethod
    def complete(cls, email, token, first_name):
        obj = cls(email, token)
        obj.first_name = first_name

        return obj
