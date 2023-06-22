#!/usr/bin/python3
"""Start link class to table in database
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """state class definition"""
    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
