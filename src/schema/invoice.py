from pydantic import BaseModel
from typing import Optional

class SchemaInvoiceHeaderUpdate(BaseModel):
    due_date: Optional[str]
    invoice_status: Optional[str]
    user_id: Optional[str]
    active_flag: Optional[str]

    class Config:
        orm_mode = True


class SchemaInvoiceLine(BaseModel):
    invoice_id: str
    book_id: str
    price: float
    quantity: int
    
    class Config:
        orm_mode = True

class SchemaInvoiceLineUpdate(BaseModel):
    book_id: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    active_flag: Optional[str]

    class Config:
        orm_mode = True