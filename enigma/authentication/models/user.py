class User(object):
    
    def __init__(self, username, password_hash):
        self.username = str(username)
        self.password_hash = str(password_hash)
    
    def serialize(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }
