from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


def connect_to_db() -> AsyncIOMotorCollection:
    mongo_db_hostname = getenv("MONGODB_HOSTNAME")
    mongo_db_login = getenv("MONGODB_USERNAME")
    mongo_db_password = getenv("MONGODB_PASSWORD")

    credentials = (
        f"{mongo_db_login}:{mongo_db_password}@"
        if all([mongo_db_login, mongo_db_password])
        else ""
    )

    mongo_uri = f"mongodb://{credentials}{f"{mongo_db_hostname}:27017" if mongo_db_hostname else "localhost:27017"}"

    return AsyncIOMotorClient(mongo_uri)["onetime-secret-api-table"][
        "onetime-secret-api-collection"
    ]
