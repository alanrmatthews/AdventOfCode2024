""" Utility functions for file processing. """

import typing
import re


def get_int_lines(file_path: str) -> typing.Generator[list[int]]:
    """Read the file at the given path and yields a list of integers for each line in the file (whitespace separated)."""
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            yield [int(value) for value in line.split()]


def get_character_lines(input_file: str) -> list[list[chr]]:
    """Read the file at the given path and return a list of characters for each line in the file."""
    with open(input_file, encoding="utf-8") as file:
        return [list(line.strip()) for line in file]


def get_character_lines_and_elements(input_file: str, pattern: str) -> tuple:
    """Reads the file in a list of characters and also return a dictionary of element locations in the list."""
    output_list = []
    element_locations = {}

    regex = re.compile(pattern)
    with open(input_file, encoding="utf-8") as file:
        for line in file:
            for match in regex.finditer(line):
                element_locations.setdefault(match.group(), set()).add((len(output_list), match.start()))

            output_list.append(list(line.strip()))

    return output_list, element_locations


def in_bounds(grid: list[list], pos: tuple[int, int]) -> bool:
    """Returns True if the tuple is in bounds of the grid."""
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])
