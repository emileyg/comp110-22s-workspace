"""An example of dictionary in EX06."""

__author__ = "730388479"


def invert(org_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the order of every other item."""
    inverted: dict[str, str] = {}
    for key in org_dict:
        if org_dict[key] not in inverted:
            inverted[org_dict[key]] = key
        else:
            raise KeyError("Key Error")
    return inverted


def favorite_color(fav_color: dict[str, str]) -> str:
    """Returns the most frequent favorite color, or first color in the case of ties."""
    col_dict: dict[str, int] = {}
    color: str = ""
    counter: int = 0
    for key in fav_color:
        if fav_color[key] not in col_dict:
            col_dict[fav_color[key]] = 1
        else:
            col_dict[fav_color[key]] += 1
    for key in col_dict:
        if col_dict[key] > counter:
            counter = col_dict[key]
            color = key
    return color


def count(a: list[str]) -> dict[str, int]:
    """Returns the amount of times a key was in the input list."""
    count_dict: dict[str, int] = {}
    for key in a:
        if key not in count_dict:
            count_dict[key] = 1
        else:
            count_dict[key] += 1
    return count_dict