from pydantic import BaseModel


class AccountBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int

    class Config:
        from_attributes = True
