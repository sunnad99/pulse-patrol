from pydantic import BaseModel


class CustomerBase(BaseModel):
    first_name: str
    last_name: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True
