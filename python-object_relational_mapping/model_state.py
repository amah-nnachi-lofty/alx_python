#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an instance Base = declarative_base():

Start link class to table in database.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of Base from declarative_base
Base = declarative_base()

# Define the State class, inheriting from Base
class State(Base):
    __tablename__ = 'states'  # Links the class to the states table in the database
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Establish a database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create the states table
    Base.metadata.create_all(engine)

