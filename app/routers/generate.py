from urllib.parse import quote

from fastapi import APIRouter, HTTPException

from ..logic import CryptoHandler, db
from ..shemas import SecretRecord
from .response import generate_responses

router = APIRouter()


@router.post(
    "/generate",
    summary="Generate Secret Record",
    description="Generate a secret record and store it in the database.",
    responses=generate_responses,
)
async def generate_record(body: SecretRecord):
    """
    Generate a secret record and store it in the database.

    - **secret**: Your secret value.
    - **secret_phrase**: Your secret phrase.

    Returns the generated secret key.
    """
    if body.secret is None or body.secret_phrase is None:
        raise HTTPException(
            400,
            "Missing required fields. Make sure to send 'secret' and 'secret_phrase' in the request body.",
        )

    encrypted_secret, secret_phrase = CryptoHandler.encrypt_record(
        body.secret, body.secret_phrase
    )

    try:
        await db.insert_secret_record(encrypted_secret, secret_phrase)
        return {"secret_key": quote(encrypted_secret, "")}
    except Exception as err:
        raise HTTPException(
            500, f"Failed to insert this record into the database:\n{err}"
        )
