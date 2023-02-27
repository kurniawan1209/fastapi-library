from src.model.base import *

class ModelPaymentMethod(Base):
    __tablename__ = "t_payment_methods"
    payment_method_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(length=20), nullable=False)
    description = Column(Text)
    tax_price = Column(Float(precision=2))
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by, last_update_by, inactive_by])


class ModelPayment(Base):
    __tablename__ = "t_payments"
    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    payment_num = Column(String(length=100), nullable=False)
    price = Column(Float(precision=2))
    payment_method_id = Column(UUID(as_uuid=True), ForeignKey("t_payment_methods.payment_method_id"))
    paid_flag = Column(Boolean, default=False)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("t_invoice_headers.invoice_id"))
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by, last_update_by, inactive_by])
    relationship("ModelPaymentMethod", foreign_keys=[payment_method_id])