from src.model.base import *

class ModelUserRole(Base):
    __tablename__ = "t_user_roles"
    role_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(length=100), nullable=False)
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


class ModelUser(Base):
    __tablename__ ="t_users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_name = Column(String(length=100), nullable=True, unique=True)
    password = Column(String, nullable=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("t_user_roles.role_id"))
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String(length=1))
    address = Column(Text)
    birth_date = Column(Date)
    created_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    last_update_date = Column(DateTime(timezone=True))
    last_update_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    inactive_by = Column(UUID(as_uuid=True), ForeignKey("t_users.user_id"))

    relationship("src.model.user.ModelUser", foreign_keys=[created_by])
    relationship("src.model.user.ModelUser", foreign_keys=[last_update_by])
    relationship("src.model.user.ModelUser", foreign_keys=[inactive_by])
    relationship("ModelUserRole", foreign_keys=[role_id])