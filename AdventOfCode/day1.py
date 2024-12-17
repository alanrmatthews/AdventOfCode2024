""" Advent of Code 2023 Day 1 """

from AdventOfCode import utilities


def build_lists(input_file: str) -> tuple:
    """Parses the input and builds the lists of integers."""
    left = []
    right = []

    for int_line in utilities.get_int_lines(input_file):
        left.append(int_line[0])
        right.append(int_line[1])

    return left, right


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    left, right = build_lists(input_file)
    return str(sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))]))


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    left, right = build_lists(input_file)
    return str(sum([a * right.count(a) for a in left]))
