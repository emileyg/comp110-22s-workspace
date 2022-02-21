"""EX05 - list Utility Functions."""

__author__ = "730388479"


def only_evens(x: list[int]) -> list[int]:
    """Given a list, returns a list of integers containning only the even inputs."""
    even_list: list[int] = list()
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            even_list.append(x[i])
        i += 1
    return even_list


def sub(given: list[int], start: int, end: int) -> list[int]:
    """Given a list and start & end index, returns a list of integers between start and end (not inclusive)."""
    start_to_end: list[int] = list()
    if start < 0:
        start = 0
    if end > len(given):
        end = len(given)
    if len(given) == 0 or start > len(given) or end <= 0:
        return start_to_end    
    while start < end:
        start_to_end.append(given[start])
        start += 1
    return start_to_end


def concat(x: list[int], y: list[int]) -> list[int]:
    """Given two lists, returns a list of both lists."""
    new_list: list[int] = list()
    new_list = x + y
    return new_list
