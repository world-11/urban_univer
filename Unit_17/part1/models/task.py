from app.backend.db import Base
from app.models import *
from sqlalchemy import Integer, String, ForeignKey, Column, Boolean
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))


