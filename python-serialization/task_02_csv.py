#!/usr/bin/env python3
"""Module that converts CSV data to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to data.json and returns True if it works."""
    try:
        with open(csv_filename, newline="", encoding="UTF-8") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="UTF-8") as f:
            json.dump(rows, f)
    except OSError:
        return False
    return True
