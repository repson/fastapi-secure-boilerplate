from fastapi import APIRouter, Depends

from app.api.endpoints import items, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(items.router, tags=["items"], prefix="/items")
api_router.include_router(users.router, tags=["users"], prefix="/users")
api_router.include_router(utils.router, tags=["utils"], prefix="/utils")