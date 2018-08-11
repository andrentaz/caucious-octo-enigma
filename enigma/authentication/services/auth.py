from authentication.services.user import user_service
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


class AuthService(object):

    def generate_auth_token(self, user, secret_key, ttl):
        s = Serializer(secret_key, expires_in=ttl)
        return s.dumps({'email': user.email})

    def verify_auth_token(self, token, secret_key):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired one
        except BadSignature:
            return None # invalid token

        user = user_service.get_user(data["email"])
        return user

auth_service = AuthService()
