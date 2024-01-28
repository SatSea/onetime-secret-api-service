from typing import Tuple

from app.logic.CryptoHandler.decrypting.decrypter import decrypt_secret
from app.logic.CryptoHandler.encrypting.encrypting import encrypt_secret
from app.logic.CryptoHandler.hashing.hashing import (
    secret_phrase_hash_for_encrypting,
    secret_phrase_hash_for_storage,
)


class CryptoHandler:
    """
    This class handles cryptographic operations for secrets using secret phrases.

    Methods:
        encrypt_record: Encrypts a secret using a secret phrase and returns the encrypted secret and a hashed version of the secret phrase.
        hash_secret_phrase: Computes and returns a hashed version of a secret phrase for storage.
        decrypt_secret: Decrypts an encrypted secret using a secret phrase.
    """

    @staticmethod
    def encrypt_record(secret: str, secret_phrase: str) -> Tuple[str, str]:
        """
        Encrypts the given secret using a hashed version of the secret phrase.

        The secret is encrypted using a hash of the secret phrase specifically tailored for encryption.
        Additionally, the method computes and returns a hash of the secret phrase suitable for secure storage.

        Args:
            secret (str): The secret to be encrypted.
            secret_phrase (str): The phrase used to encrypt the secret.

        Returns:
            Tuple[str, str]: A tuple containing the encrypted secret and the hashed secret phrase for storage.
        """

        encrypted_secret = encrypt_secret(
            secret,
            secret_phrase_hash_for_encrypting(secret_phrase),
        ).replace("/", "$")  # make secret key more url-friendly, bc it will be in url
        hashed_phrase = secret_phrase_hash_for_storage(secret_phrase)

        return encrypted_secret, hashed_phrase

    @staticmethod
    def hash_secret_phrase(secret_phrase: str) -> str:
        """
        Hashes the given secret phrase for secure storage.

        This method is used to generate a hashed version of the secret phrase, suitable for storage, ensuring that the original phrase isn't stored in plain text.

        Args:
            secret_phrase (str): The secret phrase to be hashed.

        Returns:
            str: The hashed version of the secret phrase.
        """

        return secret_phrase_hash_for_storage(secret_phrase)

    @staticmethod
    def decrypt_secret(encrypted_secret: str, secret_phrase: str) -> str:
        """
        Decrypts the given encrypted secret using the secret phrase.

        The method uses a hash of the secret phrase tailored for decryption to decrypt the provided encrypted secret.

        Args:
            encrypted_secret (str): The secret that was encrypted.
            secret_phrase (str): The phrase used for decrypting the encrypted secret.

        Returns:
            str: The decrypted secret.
        """

        decrypted_secret = decrypt_secret(
            encrypted_secret.replace("$", "/"),
            secret_phrase_hash_for_encrypting(secret_phrase),
        )

        return decrypted_secret
