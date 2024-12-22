""" Advent of Code 2024 Day 2 """

import re
import operator


def is_possible(goal: int, values: list[int], operators: list, accumulator: int) -> bool:
    """Returns True if an equation is possible, False otherwise."""

    if len(values) == 0:
        return accumulator == goal

    for op in operators:
        temp = op(accumulator, values[0])

        if temp > goal:
            continue

        if is_possible(goal, values[1:], operators, temp):
            return True

    return False


def concat(a: int, b: int) -> int:
    """Concatenates two numbers."""
    return int(f"{a}{b}")


def compute(input_file: str, operators: list) -> str:
    """Computes the solution for the given input file and operators."""
    num_possible = 0
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            m = re.findall(r"(\d+)", line.rstrip())
            values = list(map(int, m))

            if is_possible(values[0], values[2:], operators, values[1]):
                num_possible += values[0]

    return str(num_possible)


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    return compute(input_file, [operator.add, operator.mul])


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    return compute(input_file, [operator.add, operator.mul, concat])
