#!/usr/bin/python3
""" Script that prints the first State object from the database """
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    id_state = session.query(State).filter(State.name.like(
        '%s' % (sys.argv[4], ))).first()
    if id_state is None:
        print("Not found")
    else:
        print(id_state.id)
    session.close()
