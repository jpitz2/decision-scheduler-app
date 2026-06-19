# Task table defined as python class using SQLAlchemy

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime, timezone

from database import Base

# Task Model --> column_name = Column(Type, options...)
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    priority = Column(String, nullable=False)   # High, Medium, Low
    creation_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    duration = Column(Integer)
    # deadline = Column(DateTime)
    completion_status = Column(Boolean, default=False)
