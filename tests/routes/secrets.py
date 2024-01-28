import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


class TestSecretsRouter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    @patch("app.logic.db.DB.search_for_secret_phrase")
    @patch("app.logic.CryptoHandler.crypto_handler.CryptoHandler.decrypt_secret")
    def test_get_secret(self, mock_decrypt_secret, mock_search_for_secret_phrase):
        mock_search_for_secret_phrase.return_value = {"1c3a16edd92af67e55ae4162f12b350238e493c3dfc4ae706b146b33690136f6": "encrypted_secret"}
        mock_decrypt_secret.return_value = "decrypted_secret"

        secret_key = "some_encoded_key"
        response = self.client.post(
            f"/secrets/{secret_key}", json={"secret_phrase": "phrase"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"secret": "decrypted_secret"})

        response = self.client.post(
            f"/secrets/{secret_key}", json={"secret_phrase": None}
        )
        self.assertEqual(response.status_code, 400)

        mock_search_for_secret_phrase.return_value = None
        response = self.client.post(
            f"/secrets/{secret_key}", json={"secret_phrase": "phrase"}
        )
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
