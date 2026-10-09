#!/usr/bin/env python3
"""Module that serializes and deserializes a custom class with pickle."""
import pickle


class CustomObject:
    """Class that stores a name, an age and a student status."""

    def __init__(self, name, age, is_student):
        """Sets the name, age and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Saves the object to a file with pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except OSError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads an object from a file, or returns None if it fails."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
