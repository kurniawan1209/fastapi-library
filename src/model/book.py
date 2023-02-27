from src.model.base import *


class ModelBookType(Base):
    __tablename__ = "t_book_types"
    type_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(length=50), nullable=False)
    description = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by])
    relationship("src.model.user.ModelUser", foreign_keys=[last_update_by])
    relationship("src.model.user.ModelUser", foreign_keys=[inactive_by])


class ModelBook(Base):
    __tablename__ = 't_books'
    book_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), default=func.now())
    title = Column(String(length=100), nullable=False)
    description = Column(Text, nullable=True)
    type_id = Column(UUID(as_uuid=True), ForeignKey('t_book_types.type_id'))
    price = Column(Float(precision=2), nullable=False)
    stock = Column(Integer)
    image = Column(String(length=200))
    type_id = Column(UUID(as_uuid=True), ForeignKey("t_book_types.type_id"))
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by])
    relationship("src.model.user.ModelUser", foreign_keys=[last_update_by])
    relationship("src.model.user.ModelUser", foreign_keys=[inactive_by])
    relationship("ModelBookType", foreign_keys=[type_id])