from pydantic import BaseModel, Field


class SecretRecord(BaseModel):
    secret: str | None = Field(
        examples=[
            "Hello world! I'am secret, i will be encrypted by 64 bits of hashed secret phrase."
        ]
    )
    secret_phrase: str | None = Field(
        examples=[
            "Hello world! I'am secret phrase, i will be getting hashed and reduced to 64 bits to encrypt secret and when decrypt it."
        ]
    )
