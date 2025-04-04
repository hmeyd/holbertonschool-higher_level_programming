#!/usr/bin/python3
"""Add the State object “Louisiana” to the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print("{}".format(louisiana.id))

    session.close()
