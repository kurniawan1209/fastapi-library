from pydantic import BaseModel
from typing import Optional

class SchemaPaymentMethod(BaseModel):
    name: str
    description: str
    tax_price: float

    class Config:
        orm_mode = True

class SchemaPaymentMethodUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    tax_price: Optional[float]
    active_flag: Optional[str]

    class Config:
        orm_mode = True

        

class SchemaPayment(BaseModel):
    payment_method_id: str
    invoice_id: str
    
    class Config:
        orm_mode = True