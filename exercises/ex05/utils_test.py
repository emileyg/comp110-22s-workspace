"""EX05 - list Utility Functions, Tests for Functions."""

__author__ = "730388479"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


# 3 Test functions for only_evens
def test_only_evens_empty() -> None:
    """Testing for edge case, empty list."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_only_evens_use_one() -> None:
    """Testing for use case one, list of one even."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_use_two() -> None:
    """Testing for use case two, all evens."""
    xs: list[int] = [2, 2, 2]
    assert only_evens(xs) == [2, 2, 2]


# 3 Test functions for sub
def test_sub_empty() -> None:
    """Testing for edge case, empty list."""
    xs: list[int] = list()
    assert sub(xs, 3, 5) == []


def test_sub_use_one() -> None:
    """Testing for use case one, normal use."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_use_two() -> None:
    """Testing for use case two, incorrect range."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -1, 6) == [10, 20, 30, 40]


# 3 Test functions for concat
def test_concat_empty() -> None:
    """Testing for edge case, empty lists."""
    xs: list[int] = list()
    ys: list[int] = list()
    assert concat(xs, ys) == []


def test_concat_use_one() -> None:
    """Testing for use case."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5]
    assert concat(xs, ys) == [1, 2, 3, 4, 5]


def test_concat_use_two() -> None:
    """Testinf for another use case."""
    xs: list[int] = [10, 1, 52]
    ys: list[int] = [14, 2]
    assert concat(xs, ys) == [10, 1, 52, 14, 2]