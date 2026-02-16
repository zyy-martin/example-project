from sqlalchemy import Column, Integer, String
from .connection import Base

class TestResponse(Base):
    __tablename__ = "test_responses"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    version = Column(String)
