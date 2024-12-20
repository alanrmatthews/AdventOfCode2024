""" Utility functions for file processing. """

import typing


def get_int_lines(file_path: str) -> typing.Generator[list[int]]:
    """Read the file at the given path and yields a list of integers for each line in the file (whitespace separated)."""
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            yield [int(value) for value in line.split()]


def get_character_lines(input_file: str) -> list[list[chr]]:
    """Read the file at the given path and return a list of characters for each line in the file."""
    with open(input_file, encoding="utf-8") as file:
        return [list(line.strip()) for line in file]
