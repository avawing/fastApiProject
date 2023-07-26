from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel
from sqlalchemy.orm import Session


class User(BaseModel):
    first_name: str
    last_name: Union[str, None] = None
    email: str
    has_loan: bool
    has_other_loan: bool

    class Config:
        orm_mode = True


router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(db: Session) -> [User]:
    return db.query(User).all()


@router.post("/users/", tags=["users"])
async def create_user(db: Session, user: User) -> User:
    db_user = User(first_name=user.first_name,
                   last_name=user.last_name,
                   email=user.email,
                   has_loan=user.has_loan,
                   has_other_loat=user.has_other_loan)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", tags=["users"])
async def read_user(db: Session, user_id: int) -> User:
    user = await db.query(User).filter(User.id == user_id).first()
    return user


@router.put("/users/{user_id}", tags=["users"])
async def update_user(db: Session, user_id: int, user: User) -> User:
    db_user = await db.query(User).filter(User.id == user_id).first()

    for k, v in db_user:
        if db_user[k] != user[k]:
            db_user[k] = user[k]

    db .add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/users/{user_id}", tags=["users"])
async def delete_user(db: Session, user_id: int) -> bool:
    user = await db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return True
