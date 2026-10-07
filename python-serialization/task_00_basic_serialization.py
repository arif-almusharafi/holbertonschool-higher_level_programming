#!/usr/bin/env python3
"""Module that works with JSON files."""
import json


def serialize_and_save_to_file(data, filename):
    """writes a dictionary to a file as JSON."""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Reads a JSON file and returns a dictionary"""
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
