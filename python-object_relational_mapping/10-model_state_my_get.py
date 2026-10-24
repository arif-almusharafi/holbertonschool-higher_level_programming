#!/usr/bin/python3
"""Script that prints the id of the State with the name given as argument."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    state = session.query(State).filter(
        func.binary(State.name) == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
