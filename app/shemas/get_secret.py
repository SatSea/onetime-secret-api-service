from pydantic import BaseModel, Field


class GetSecret(BaseModel):
    secret_phrase: str | None = Field(
        examples=[
            "Hello world! I'am secret phrase, i will be getting hashed and reduced to 64 bits to encrypt secret and when decrypt it."
        ]
    )
