from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt_secret(encrypted_secret: str, hashed_secret_phrase: bytes) -> str:
    cipher = AES.new(hashed_secret_phrase, AES.MODE_ECB)

    decrypted_data = cipher.decrypt(b64decode(encrypted_secret))

    unpadded_data = unpad(decrypted_data, AES.block_size)

    return unpadded_data.decode()
