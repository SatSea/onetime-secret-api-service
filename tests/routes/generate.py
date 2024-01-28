import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

class TestGenerateRouter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    @patch("app.logic.db.DB.insert_secret_record")
    @patch("app.logic.CryptoHandler.crypto_handler.CryptoHandler.encrypt_record")
    def test_generate_record(self, mock_encrypt_record, mock_insert_secret_record):
        mock_encrypt_record.return_value = ("encrypted_secret", "secret_phrase_hash")
        mock_insert_secret_record.return_value = None

        response = self.client.post(
            "/generate", json={"secret": "mysecret", "secret_phrase": "phrase"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("secret_key", response.json())

        response = self.client.post(
            "/generate", json={"secret": None, "secret_phrase": "phrase"}
        )
        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            "/generate", json={"secret": "mysecret", "secret_phrase": None}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
