# imports
# imports 
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.types import JSON as Dictionary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create ORM classes

Base = declarative_base()

class Gold(Base):
    __tablename__ = 'gold'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    date = Column(String, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

class Silver(Base):
    __tablename__ = 'silver'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    date = Column(String, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

class Platinum(Base):
    __tablename__ = 'platinum'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    date = Column(String, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

class Palladium(Base):
    __tablename__ = 'palladium'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    date = Column(String, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

class Copper(Base):
    __tablename__ = 'copper'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    date = Column(String, primary_key=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

class Statistics(Base):
    __tablename__ = 'statistics'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    id = Column(Integer, primary_key=True)
    metal = Column(String)
    stat_type = Column(String)
    column = Column(String)
    value = Column(Float)
    start_date = Column(String)
    end_date = Column(String)
    generated_at = Column(String)

class Predictions(Base):
    __tablename__ = 'predictions'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    id = Column(Integer, primary_key=True)
    metal = Column(String)
    algorithm = Column(String)
    prediction = Column(Float)
    predicted_date = Column(String)
    generated_at = Column(String)

class Visualizations(Base):
    __tablename__ = 'visualizations'
    __table_args__ = {'extend_existing': True, 'schema': 'final'}
    id = Column(Integer, primary_key=True)
    metal = Column(String)
    visual_type = Column(String)
    parameters = Column(Dictionary)
    file_path = Column(String)
    generated_at = Column(String)

# create engine

# postgres db conn vars
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
db_user = 'postgres'
db_pass = 'password'

# create engine
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

# create tables
Base.metadata.create_all(engine)

# session
Session = sessionmaker(bind=engine)
session = Session()