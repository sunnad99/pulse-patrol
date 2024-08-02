from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud, model, schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/customers/", response_model=schema.Customer)
def create_customer(user: schema.CustomerCreate, db: Session = Depends(get_db)):

    return crud.create_customer(db=db, customer=user)


@router.get("/customers/", response_model=list[schema.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


@router.get("/customers/{customer_id}", response_model=schema.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_customer(db, customer_id=customer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
