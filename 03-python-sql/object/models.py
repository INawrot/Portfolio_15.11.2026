from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
ORM_DB_PATH = "sqlite:///adidas_orm.db"

class CountryDim(Base):
    __tablename__ = 'country_dim'
    country_code = Column(String, primary_key=True)
    currency = Column(String)
    shoe_metric = Column(String)

class ShoesDim(Base):
    __tablename__ = 'shoes_dim'
    id = Column(String, primary_key=True)
    name = Column(String)
    best_for_wear = Column(String)
    gender = Column(String)
    dominant_color = Column(String)

class ShoesFact(Base):
    __tablename__ = 'shoes_fact'
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String, ForeignKey('shoes_dim.id'))
    size = Column(String)
    price = Column(Float)
    country_code = Column(String, ForeignKey('country_dim.country_code'))
    date = Column(String)
