#!/usr/bin/python3
"""Script that prints all City objects with the name of their State."""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
