#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    print(f"{state.id}: {state.name}" if state else "Nothing")

    session.close()
