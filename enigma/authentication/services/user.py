from passlib.apps import custom_app_context as pwd_context
from authentication.repositories.user import user_repository


class UserService(object):

    class EmailAlreadyUsed(Exception):
        pass

    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def create_user(self, email, password):
        password_hash = pwd_context.encrypt(password)

        try:
            user = self.user_repository.create_user(email, password_hash)
        except self.user_repository.DuplicateUserError:
            raise self.EmailAlreadyUsed()
        
        return user

    def get_user(self, email):
        return self.user_repository.get_by_email(email)

    def verify_password(self, email, password):
        user = self.user_repository.get_by_email(email)

        return user and pwd_context.verify(password, user.password_hash)

user_service = UserService(user_repository)
