import unittest

from app.shemas import GetSecret


class TestGetSecretSchema(unittest.TestCase):
    def test_valid_get_secret(self):
        get_secret = GetSecret(secret_phrase="validphrase")
        self.assertEqual(get_secret.secret_phrase, "validphrase")

        get_secret = GetSecret(secret_phrase=None)
        self.assertIsNone(get_secret.secret_phrase)


if __name__ == "__main__":
    unittest.main()
