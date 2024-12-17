""" Utility functions for file processing. """

import typing


def get_int_lines(file_path: str) -> typing.Generator[list[int]]:
    """Read the file at the given path and yields a list of integers for each line in the file (whitespace separated)."""
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            yield [int(value) for value in line.split()]
