from typing import Any, Dict


secrets_responses: Dict[int | str , Dict[str, Any]] = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {"example": {"detail": "Invalid request data"}}
        },
    },
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"detail": "Can't find secret with this secret code and phrase"}}},
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["field_name", 0],
                            "msg": "Validation error message",
                            "type": "Validation error type",
                        }
                    ]
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {"detail": "Internal server error occurred"}
            }
        },
    },
}
