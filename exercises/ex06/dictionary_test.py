"""A test for dictionary in EX06."""

__author__ = "730388479"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count


# Tests for invert
def test_invert_edge_empty() -> None:
    """Testing for edge case, empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_use_one() -> None:
    """Testing for use case one, simple inversion."""
    xs: dict[str, str] = {"hi": "bye"}
    assert invert(xs) == {"bye": "hi"}


def test_invert_use_two() -> None:
    """Testing for use case two, complex inversion."""
    xs: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(xs) == {"b": "a", "d": "c", "f": "e"}


# Tests favorite_color
def test_favorite_color_edge_empty() -> None:
    """Testing for edge case, empty dictionary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == {}


def test_favorite_color_use_one() -> None:
    """Testing for use case one, obvious most frequent color."""
    xs: dict[str, str] = {"Em": "purple", "Andy": "blue", "Jen": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_use_two() -> None:
    """Testing for use case two, less obvious most frequent color."""
    xs: dict[str, str] = {"Em": "purple", "Andy": "blue", "Jen": "blue", "Maggie": "purple"}
    assert favorite_color(xs) == "purple"


# Tests count
def test_count_edge() -> None:
    """Testing for edge case, empty dictionary."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_use_one() -> None:
    """Testing for use case one, no repeats."""
    xs: list[str] = ["bat", "cat", "rat"]
    assert count(xs) == {"bat": 1, "cat": 1, "rat": 1}


def test_count_use_two() -> None:
    """Testing for use case two, repeats."""
    xs: list[str] = ["bat", "bat", "rat"]
    assert count(xs) == {"bat": 2, "rat": 1}
