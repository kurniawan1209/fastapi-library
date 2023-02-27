from pydantic import BaseModel
from typing import Optional


class SchemaBookType(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class SchemaBookTypeUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    active_flag: Optional[bool]

    class Config:
        orm_mode = True


class SchemaBook(BaseModel):
    title: str
    description: str
    type_id: str
    price: float
    stock: int
    image: str
    type_id: str

    class Config:
        orm_mode = True

class SchemaBookUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    type_id: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    image: Optional[str]
    type_id: Optional[str]
    active_flag: Optional[bool]

    class Config:
        orm_mode = True