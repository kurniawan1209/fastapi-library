from src.model.base import *

class ModelInvoiceHeader(Base):
    __tablename__ = "t_invoice_headers"
    invoice_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    invoice_num = Column(String(20), nullable=False)
    due_date = Column(DateTime)
    invoice_status = Column(String(length=1))
    user_id = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by, last_update_by, inactive_by, user_id])


class ModelInvoiceLine(Base):
    __tablename__ = "t_invoice_lines"
    invoice_line_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("t_invoice_headers.invoice_id"))
    book_id = Column(UUID(as_uuid=True), ForeignKey("t_books.book_id"))
    price = Column(Float(precision=2))
    quantity = Column(Integer)
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by, last_update_by, inactive_by])
    relationship("src.model.book.ModelBook", foreign_keys=[book_id])
