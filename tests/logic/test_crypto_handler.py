import unittest

from app.logic import CryptoHandler


class TestCryptoHandler(unittest.TestCase):
    def test_encrypt_record(self):
        secret = "Hello world! I'am secret, i will be encrypted by 64 bits of hashed secret phrase."
        secret_phrase = "Hello world! I'am secret phrase, i will be getting hashed and reduced to 64 bits to encrypt secret."
        encrypted_secret, hashed_phrase = CryptoHandler.encrypt_record(
            secret, secret_phrase
        )

        self.assertEqual(
            encrypted_secret,
            "CSkzqhAGcpz16PA0qlGWGmyGiIt04pz7Xq$1LxKdv$KbzYz$5wJSwf9EHWtYTZEqUsfwSWgjWNyeC4Y+$WempeZyVQZRDR+FtBFtRqsUpe4wkqM2oMYnMU2wanFgx84o",
        )
        self.assertEqual(
            hashed_phrase,
            "0fd69245f2faf10a82e4265b5c326da920feea897048bfa924bd035df967f19d",
        )

    def test_hash_secret_phrase(self):
        secret_phrase = "Hello world! I'am secret phrase, i will be getting hashed and reduced to 64 bits to encrypt secret."
        hashed_phrase = CryptoHandler.hash_secret_phrase(secret_phrase)

        secret = "Hello world! I'am secret, i will be encrypted by 64 bits of hashed secret phrase."
        encrypted_secret, hashed_phrase_in_record = CryptoHandler.encrypt_record(
            secret, secret_phrase
        )

        self.assertEqual(hashed_phrase, hashed_phrase_in_record)

    def test_decrypt_secret(self):
        secret = "my_secret"
        secret_phrase = "my_secret_phrase"
        encrypted_secret, _ = CryptoHandler.encrypt_record(secret, secret_phrase)
        decrypted_secret = CryptoHandler.decrypt_secret(encrypted_secret, secret_phrase)

        self.assertEqual(decrypted_secret, secret)


if __name__ == "__main__":
    unittest.main()
