import os
from task2.solution_2 import write_to_csv
import csv


def test_write_to_css():
    test_data = {"A": 4, "B": 8}
    write_to_csv(test_data)
    assert os.path.exists("./task2/beasts.csv")


def test_write_to_csv_content():
    test_data = {"A": 4, "B": 8}
    write_to_csv(test_data)

    with open("./task2/beasts.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        contents = {rows[0]: int(rows[1]) for rows in reader}

        assert contents["A"] == 4
        assert contents["B"] == 8
