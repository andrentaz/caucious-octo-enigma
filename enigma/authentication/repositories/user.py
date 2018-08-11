from pymongo import errors

from authentication import models
from authentication import mongo

class UserRepository(object):

    class DuplicateUserError(Exception):
        pass

    def create_user(self, email, pwd_hash):
        user = models.User(
            email=email,
            password_hash=pwd_hash
        )

        try:
            self._collection().save(user.serialize())
        except errors.DuplicateKeyError:
            raise self.DuplicateUserError()
        return user

    def get_by_email(self, email):
        return models.User.loads(
            **self._collection().find_one({"email": email})
        )
    
    @classmethod
    def _collection(cls):
        return mongo.db.users

user_repository = UserRepository()
