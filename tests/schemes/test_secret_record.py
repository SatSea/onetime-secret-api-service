import unittest

from app.shemas import SecretRecord


class TestSecretRecordSchema(unittest.TestCase):
    def test_valid_secret_record(self):
        secret_record = SecretRecord(secret="somesecret", secret_phrase="validphrase")
        self.assertEqual(secret_record.secret, "somesecret")
        self.assertEqual(secret_record.secret_phrase, "validphrase")

        secret_record = SecretRecord(secret=None, secret_phrase=None)
        self.assertIsNone(secret_record.secret)
        self.assertIsNone(secret_record.secret_phrase)


if __name__ == "__main__":
    unittest.main()
