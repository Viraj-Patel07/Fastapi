from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base




class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(Text)