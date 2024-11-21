import os
from task2.solution_2 import AnimalCounter
import csv
import tempfile
import pytest


@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", newline="", encoding="utf-8"
    ) as temp_file:
        yield temp_file.name
    os.remove(temp_file.name)


def test_write_to_css(temp_csv_file):
    test_data = {"A": 4, "B": 8}

    AnimalCounter().write_to_csv(test_data, temp_csv_file)

    assert os.path.exists(temp_csv_file)


def test_write_to_csv_content(temp_csv_file):
    test_data = {"A": 4, "B": 8}
    AnimalCounter().write_to_csv(test_data, temp_csv_file)

    with open(temp_csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        contents = {rows[0]: int(rows[1]) for rows in reader}

        assert contents["A"] == 4
        assert contents["B"] == 8
