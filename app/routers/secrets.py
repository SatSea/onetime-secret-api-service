from urllib.parse import unquote

from fastapi import APIRouter, HTTPException
from fastapi.openapi.models import Response

from ..logic import CryptoHandler, db
from ..shemas import GetSecret
from .response import secrets_responses

router = APIRouter()


@router.post(
    "/secrets/{secret_key}",
    summary="Get Secret",
    description="Retrieve a secret using a secret key and secret phrase.",
    responses=secrets_responses,
    response_description="Decrypted secret value",
)
async def get_secret(secret_key: str, body: GetSecret):
    """
    Retrieve a secret using a secret key and secret phrase.

    - **secret_phrase**: Your secret phrase.

    Returns the decrypted secret value.
    """
    if secret_key is None or body.secret_phrase is None:
        raise HTTPException(
            400,
            "Missing required fields. Make sure to send 'secret_key' in the path and 'secret_phrase' in the request body.",
        )

    secret_phrase_hash = CryptoHandler.hash_secret_phrase(body.secret_phrase)

    try:
        encrypted_secret = await db.search_for_secret_phrase(
            secret_phrase_hash, unquote(secret_key)
        )
    except Exception as err:
        raise HTTPException(500, f"Failed to search in the database:\n{err}")

    if encrypted_secret is None:
        raise HTTPException(404, "Can't find secret with this secret code and phrase")

    decrypted_secret = CryptoHandler.decrypt_secret(
        encrypted_secret[secret_phrase_hash], body.secret_phrase
    )

    return {"secret": decrypted_secret}
