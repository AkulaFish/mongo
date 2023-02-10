import os

from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URL"))

db = client.office

employees = db.get_collection("employees")
