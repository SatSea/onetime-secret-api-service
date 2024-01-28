from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt_secret(secret: str, hashed_secret_phrase: bytes) -> str:
    cipher = AES.new(hashed_secret_phrase, AES.MODE_ECB)
    padded_data = pad(secret.encode(), AES.block_size)

    return b64encode(cipher.encrypt(padded_data)).decode()
