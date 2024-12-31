"""Base class for Advent of Code days."""

import typing
import re


class AdventOfCodeDay:
    """Base class for Advent of Code days."""

    def __init__(self, input_file: str):
        self.input_file = input_file

    def part1(self):
        """Returns the solution for part 1 of the day."""
        raise NotImplementedError

    def part2(self):
        """Returns the solution for part 2 of the day."""
        raise NotImplementedError

    # TODO Remove file path, it is input_file
    def get_int_lines(self, file_path: str) -> typing.Generator[list[int]]:
        """Read the file at the given path and yields a list of integers for each line in the file (whitespace separated)."""
        with open(file_path, encoding="utf-8") as file:
            for line in file:
                yield [int(value) for value in line.split()]

    def get_character_lines(self) -> list[list[chr]]:
        """Read the file at the given path and return a list of characters for each line in the file."""
        with open(self.input_file, encoding="utf-8") as file:
            return [list(line.strip()) for line in file]

    def get_character_lines_and_elements(self, pattern: str) -> tuple:
        """Reads the file in a list of characters and also return a dictionary of element locations in the list."""
        output_list = []
        element_locations = {}

        regex = re.compile(pattern)
        with open(self.input_file, encoding="utf-8") as file:
            for line in file:
                for match in regex.finditer(line):
                    element_locations.setdefault(match.group(), set()).add((len(output_list), match.start()))

                output_list.append(list(line.strip()))

        return output_list, element_locations

    def in_bounds(self, grid: list[list], pos: tuple[int, int]) -> bool:
        """Returns True if the tuple is in bounds of the grid."""
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])
