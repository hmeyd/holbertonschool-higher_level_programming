#!/usr/bin/python3
"""This module defines the State class that inherits from Base"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"

engine = create_engine('mysql+mysqldb://<mysql_user>:'
'<mysql_password>@localhost:3306/<database_name>')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
new_state = State(name="California")
session.add(new_state)
session.commit()

session.close()
