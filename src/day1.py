""" Advent of Code Day 1 """

import os


def build_lists(input_file: str) -> tuple:
    """Parses the input and builds the lists of integers."""
    left = []
    right = []

    input_file = os.path.join(os.getcwd(), "inputs", input_file)

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            a, b = map(int, line.split())
            left.append(a)
            right.append(b)
    return left, right


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    left, right = build_lists(input_file)
    return str(sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))]))


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    left, right = build_lists(input_file)
    return str(sum([a * right.count(a) for a in left]))
