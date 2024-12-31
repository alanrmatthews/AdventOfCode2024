""" Advent of Code 2023 Day 1 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2023 Day 1 class"""

    def build_lists(self) -> tuple:
        """Parses the input and builds the lists of integers."""
        left = []
        right = []

        for int_line in self.get_int_lines(self.input_file):
            left.append(int_line[0])
            right.append(int_line[1])

        return left, right

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        left, right = self.build_lists()
        return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        left, right = self.build_lists()
        return sum(a * right.count(a) for a in left)
