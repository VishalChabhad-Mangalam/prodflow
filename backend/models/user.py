from sqlalchemy import Column, String, Boolean, DateTime
from core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'prodflow_core'}

    employee_id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)
    password_hash = Column(String, nullable=False)
    department = Column(String(50))
    role = Column(String(20))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)