from hashlib import sha3_256


def hash_secret_phrase(secret_phrase: str, salt: str = "", size: int = 256) -> str:
    hasher = sha3_256()
    hasher.update((secret_phrase + salt).encode())
    return hasher.hexdigest()[:size]


def secret_phrase_hash_for_storage(secret_phrase: str) -> str:
    return hash_secret_phrase(secret_phrase, "-onetime-secret-api-storage-salt")


def secret_phrase_hash_for_encrypting(secret_phrase: str) -> bytes:
    return hash_secret_phrase(
        secret_phrase, "-onetime-secret-api-encryption-salt", 32
    ).encode()
