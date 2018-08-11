class User(object):
    
    def __init__(self, email, password_hash):
        self.email = str(email)
        self.password_hash = str(password_hash)
    
    def serialize(self):
        return {
            "email": self.email,
            "password_hash": self.password_hash
        }

    @staticmethod
    def loads(**kwargs):
        return User(
            email=kwargs["email"],
            password_hash=kwargs["password_hash"]
        )
