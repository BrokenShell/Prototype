from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import MongoDB

Authentication = HTTPBasicAuth()
Users = MongoDB("Credentials")


@Authentication.verify_password
def verify_password(username, password) -> bool:
    users = Users.read({})
    #Todo: Add encryption!
    if username not in users.keys():
        return False
    hashed = generate_password_hash(users.get(username))
    return check_password_hash(hashed, password)
