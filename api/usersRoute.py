from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api import database, usersModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    has_loan: bool
    has_other_loan: bool

    class Config:
        from_attributes = True


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users(db: Session = Depends(database.get_db)) -> List[User]:
    return db.query(usersModel.User).all()


@router.post("/")
async def create_user(user: User, db: Session = Depends(database.get_db)) -> User:
    db_user = User(first_name=user.first_name,
                   last_name=user.last_name,
                   email=user.email,
                   has_loan=user.has_loan,
                   has_other_load=user.has_other_loan)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    print(db_user)
    return db_user


@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(database.get_db)) -> User:
    db_user = db.query(usersModel.User).filter(User.id == user_id).first()
    return db_user


@router.put("/{user_id}")
async def update_user(user_id: int, user: User, db: Session = Depends(database.get_db)) -> User:
    db_user = await db.query(User).filter(User.id == user_id).first()

    for k, v in db_user:
        if db_user[k] != user[k]:
            db_user[k] = user[k]

    db .add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(database.get_db)) -> bool:
    user = await db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return True
