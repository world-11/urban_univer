from app.backend import db
from app.models import *
from sqlalchemy import Integer, String, ForeignKey, Column, Boolean, Float
from sqlalchemy.orm import relationship

class User(db.Base):
    __tablename__ = "users"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

