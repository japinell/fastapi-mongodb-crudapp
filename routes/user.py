# Import statements

from fastapi import APIRouter
from models.user import User
from config.database import connection
from schemas.user import userEntity, listOfUserEntity
from bson import ObjectId

user_router = APIRouter()
@user_router.get("/users")
async def find_all_users():
    return listOfUserEntity(connection.cruddb.users.find())

@user_router.get("/users/{userId}")
async def find_user(userId):
    return userEntity(connection.cruddb.users.find_one({"_id": ObjectId(userId)}))
@user_router.post("/users")
async def create_user(user: User):
    connection.cruddb.users.insert_one(dict(user))
    return listOfUserEntity(connection.cruddb.users.find())

@user_router.put("/users/{userId}")
async def update_user(userId, user: User):
    connection.cruddb.users.find_one_and_update(
        {"_id": ObjectId(userId)},
        {"$set": dict(user)}
    )
    return userEntity(connection.cruddb.users.find_one({"_id": ObjectId(userId)}))

@user_router.delete("/users/{userId}")
async def delete_user(userId):
    return userEntity(connection.cruddb.users.find_one_and_delete(
        {"_id": ObjectId(userId)}))