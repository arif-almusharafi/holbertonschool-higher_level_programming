#!/usr/bin/python3
"""Module that defines the City class linked to the table cities."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Class that represents a row of the table cities."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
