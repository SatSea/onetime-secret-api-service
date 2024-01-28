from typing import Any, Dict

generate_responses: Dict[int | str, Dict[str, Any]] = {
    200: {
        "description": "Successful response",
        "content": {
            "application/json": {"example": {"secret_key": "example_secret_key_value"}}
        },
    },
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {"example": {"detail": "Missing required fields"}}
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {"detail": "Internal Server Error occurred"}
            }
        },
    },
}
