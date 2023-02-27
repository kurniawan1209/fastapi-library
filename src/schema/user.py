from pydantic import BaseModel
from typing import Optional

class SchemaUserRole(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True

class SchemaUserRoleUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    active_flag: Optional[bool]

    class Config:
        orm_mode = True



class SchemaUser(BaseModel):
    user_name: str
    password: str
    role_id: Optional[str]
    first_name: str
    last_name: str
    gender: str
    address: str
    birth_date: Optional[str]

    class Config:
        orm_mode = True

class SchemaUserUpdate(BaseModel):
    user_name: Optional[str]
    password: Optional[str]
    role_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    address: Optional[str]
    birth_date: Optional[str]
    active_flag: Optional[bool]

    class Config:
        orm_mode = True