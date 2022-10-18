from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import MongoDB
from app.encryption import Cypher

Authentication = HTTPBasicAuth()
Users = MongoDB("Credentials")


@Authentication.verify_password
def verify_password(username, password) -> bool:
    users = Users.read({})
    if username not in users.keys():
        return False
    decrypted = Cypher.decrypt(users.get(username))
    hashed = generate_password_hash(decrypted)
    return check_password_hash(hashed, password)


def create_user(username: str, password: str) -> bool:
    return Users.update(
        {username: {"$exists": False}},
        {username: Cypher.encrypt(password)},
    )


def create_first_user(username: str, password: str) -> bool:
    return Users.create(
        {username: Cypher.encrypt(password)},
    )
