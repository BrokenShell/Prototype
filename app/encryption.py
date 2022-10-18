from os import getenv

from dotenv import load_dotenv
from rsa import encrypt, decrypt, PublicKey, PrivateKey, newkeys


class Cypher:
    load_dotenv()
    public_key = PublicKey(
        n=int(getenv("KEY_N")),
        e=int(getenv("KEY_E")),
    )
    private_key = PrivateKey(
        n=int(getenv("KEY_N")),
        e=int(getenv("KEY_E")),
        p=int(getenv("KEY_P")),
        d=int(getenv("KEY_D")),
        q=int(getenv("KEY_Q")),
    )

    @classmethod
    def encrypt(cls, data: str) -> bytes:
        return encrypt(data.encode(), cls.public_key)

    @classmethod
    def decrypt(cls, data: bytes) -> str:
        return decrypt(data, cls.private_key).decode()


def new_keys():
    _, private_key = newkeys(512)
    output = (
        f"KEY_N={private_key.n}",
        f"KEY_E={private_key.e}",
        f"KEY_D={private_key.d}",
        f"KEY_P={private_key.p}",
        f"KEY_Q={private_key.q}",
    )
    with open("rsa.env", "w") as file:
        file.write("\n".join(output) + "\n")


if __name__ == '__main__':
    string = "right, it doesn't really throw it away, right?"
    crypto = Cypher.encrypt(string)
    print(crypto)
    normal = Cypher.decrypt(crypto)
    print()
    print(normal)
