from fastapi import FastAPI

from app.routers import generate, secrets
from app.logic.db import db

app = FastAPI()

app.include_router(generate.router)
app.include_router(secrets.router)


@app.get("/", include_in_schema=False)
@app.post("/", include_in_schema=False)
async def root():
    return {"message": "Go to /docs to get documentation about routes"}
