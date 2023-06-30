from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from app import crud, models
from app.schemas import user

router = APIRouter()


@router.get("/", response_model=List[user.User])
def read_items() -> Any:
    return {"Hello": "World"}