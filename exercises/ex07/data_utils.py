"""Dictionary related utility functions."""

__author__ = "730388479"

from csv import DictReader 

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a table N number of rows of a given table."""
    head_dict: dict[str, list[str]] = {}
    
    if len(table) <= N:
        return table
    else:
        for col in table:
            n_values: list[str] = []
            i: int = 0
            while i < N:
                n_values.append(table[col][i])
                i += 1
            head_dict[col] = n_values

        return head_dict


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Given a table and list of selected columns, produces a new table with selected columns."""
    sel_dict: dict[str, list[str]] = {}

    for col_name in columns:
        sel_dict[col_name] = table[col_name]

    return sel_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Given two column based tables, produces one column based table where the data from both are combined."""
    combine_dict: dict[str, list[str]] = {}

    for col in table_1:
        combine_dict[col] = table_1[col]

    for col in table_2:
        if col not in combine_dict:
            combine_dict[col] = table_2[col]
        else:
            combine_dict[col] = table_1[col] + table_2[col]
    
    return combine_dict


def count(list: list[str]) -> dict[str, int]:
    """Count of the frequencies of various items in a list."""
    count_dict: dict[str, int] = {}

    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict