import uuid

from sqlalchemy import Column, String

from database.connection import Base, engine

class Posts(Base):
    __tablename__ = "posts"
    id = Column(String(100), primary_key=True)
    title = Column(String(100))
    description = Column(String(100))


Base.metadata.create_all(engine)
