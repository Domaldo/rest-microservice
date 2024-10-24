import jwt
import datetime

SECRET_KEY = "the-secret-key"

def create_jwt():
    return jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=45)}, SECRET_KEY, algorithm="HS256")

def verify_jwt(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        return False
