""" Advent of Code 2024 Day 2 """

import re
import itertools
import operator


def is_possible(values: list[int], operators: list) -> bool:
    """Returns True if an equation is possible, False otherwise."""
    for permutation in itertools.product(operators, repeat=len(values) - 2):
        result = values[1]
        for i in range(len(values) - 2):
            result = permutation[i](result, values[i + 2])

        if result == values[0]:
            return True

    return False


def concat(a: int, b: int) -> int:
    """Concatenates two numbers."""
    return int(f"{a}{b}")


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    num_possible = 0
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            m = re.findall(r"(\d+)", line.rstrip())
            values = list(map(int, m))

            if is_possible(values, [operator.add, operator.mul]):
                num_possible += values[0]

    return str(num_possible)


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    num_possible = 0
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            m = re.findall(r"(\d+)", line.rstrip())
            values = list(map(int, m))

            if is_possible(values, [operator.add, operator.mul, concat]):
                num_possible += values[0]

    return str(num_possible)
