from sqlalchemy.orm import Session

from . import model, schema


def create_account(db: Session, account: schema.AccountCreate):

    db_account = model.Account(**account.model_dump())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
