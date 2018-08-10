from passlib.apps import custom_app_context as pwd_context
from authentication.repositories.user import user_repository


class UserService(object):

    class UserNotCreated(Exception):
        pass

    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def create_user(self, username, password):
        password_hash = pwd_context.encrypt(password)
        print password_hash
        user = self.user_repository.create_user(username, password_hash)

        if not user:
            raise self.UserNotCreated()
        
        return user

user_service = UserService(user_repository)
