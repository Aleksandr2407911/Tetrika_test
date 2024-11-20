import pytest

from task1.solution_1 import strict


def test_two_int():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    assert sum_two(5, 6) == 11


def test_float_int():
    @strict
    def sum_three(a: float, b: float, c: int):
        return a + b + c

    assert sum_three(4.5, 5.5, 8) == 18.0


def test_str():
    @strict
    def sum_string(a: str, b: str, c: str):
        return a + b + c

    assert sum_string("You ", "are good ", "boy") == "You are good boy"


def test_any():
    @strict
    def sum_string(a: str, b: str, c: str):
        return a + b + c

    assert sum_string("You ", "are good ", c="boy") == "You are good boy"


def test_by_error():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    with pytest.raises(
        TypeError,
    ):
        sum_two(8.7, 8)
