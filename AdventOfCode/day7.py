""" Advent of Code 2024 Day 2 """

import re
import operator

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 10 solution."""

    def is_possible(self, goal: int, values: list[int], operators: list, accumulator: int) -> bool:
        """Returns True if an equation is possible, False otherwise."""

        if len(values) == 0:
            return accumulator == goal

        for op in operators:
            temp = op(accumulator, values[0])

            if temp > goal:
                continue

            if self.is_possible(goal, values[1:], operators, temp):
                return True

        return False

    def concat(self, a: int, b: int) -> int:
        """Concatenates two numbers."""
        return int(f"{a}{b}")

    def compute(self, input_file: str, operators: list) -> str:
        """Computes the solution for the given input file and operators."""
        num_possible = 0
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                m = re.findall(r"(\d+)", line.rstrip())
                values = list(map(int, m))

                if self.is_possible(values[0], values[2:], operators, values[1]):
                    num_possible += values[0]

        return num_possible

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        return self.compute(self.input_file, [operator.add, operator.mul])

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        return self.compute(self.input_file, [operator.add, operator.mul, self.concat])
