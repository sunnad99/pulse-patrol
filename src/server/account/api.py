from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, schema

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


BASE_ROUTE = "/accounts"


@router.post(BASE_ROUTE, response_model=schema.Account)
def create_account(user: schema.AccountCreate, db: Session = Depends(get_db)):

    return crud.create_account(db=db, account=user)


# TODO: Add read endpoints once we have other frontend pages
# @router.get(BASE_ROUTE, response_model=list[schema.Account])
# def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     customers = crud.get_customers(db, skip=skip, limit=limit)
#     return customers


# @router.get("/accounts/{customer_id}", response_model=schema.Account)
# def read_customer(customer_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_account(db, customer_id=customer_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
