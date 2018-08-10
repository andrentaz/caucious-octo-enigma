from authentication import models
from authentication import mongo

class UserRepository(object):

    def create_user(self, username, pwd_hash):
        user = models.User(
            username=username,
            password_hash=pwd_hash
        )

        self._collection().save(user.serialize())
        return user
    
    @classmethod
    def _collection(cls):
        return mongo.db.users

user_repository = UserRepository()
