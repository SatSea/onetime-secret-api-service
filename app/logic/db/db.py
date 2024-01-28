from typing import Dict

from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import results

from app.logic.db.db_utils import connect_to_db


class DB:
    _db: AsyncIOMotorCollection

    def __init__(self):
        self._db = connect_to_db()

    async def search_for_secret_phrase(
        self, secret_phrase_hash: str, secret_key: str
    ) -> Dict[str, str] | None:
        return await self._db.find_one_and_delete({secret_phrase_hash: secret_key})

    async def insert_secret_record(
        self, encrypted_secret: str, secret_phrase_hash: str
    ) -> results.InsertOneResult:
        return await self._db.insert_one({secret_phrase_hash: encrypted_secret})


db = DB()
