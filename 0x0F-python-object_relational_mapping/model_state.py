#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'

        id = column(Integer NOT NULL, UNIQUE, auto_genarated, primary_key=True)
        name = column(String(128))
    Base.metadata.create_all(engine)
