from werkzeug.security import safe_str_cmp
# accesses user.py file and imports User class
from models.user import UserModel

def authenticate(username, password):
    # find user by username
    user = UserModel.find_by_username (username)
    # safe_str_cmp() compares strings
    if user and safe_str_cmp(user.password, password):
        return user

def identify(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
