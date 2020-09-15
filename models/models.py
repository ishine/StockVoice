from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class Stocks(Base):
    __tablename__ = 'stocks'
    pkey = Column(String(128), primary_key=True)
    date = Column(String(128))
    open = Column(Integer)
    high = Column(Integer)
    low = Column(Integer)
    close = Column(Integer)
    volume = Column(Integer)
    code = Column(Integer)

    def __init__(self, date=None):
        self.pkey = pkey
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.code = code


