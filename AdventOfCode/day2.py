""" Advent of Code 2024 Day 2 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 2 solution."""

    def is_safe(self, values: str, bad_levels_allowed: int = 0) -> bool:
        """Returns True if the line is safe, False otherwise."""
        positives = 0
        negatives = 0

        for lhs, rhs in zip(values, values[1:]):
            difference = lhs - rhs

            if 0 < difference < 4:
                positives += 1
            elif 0 > difference > -4:
                negatives += 1

        expected = len(values) - 1

        safe = positives == expected or negatives == expected

        if not safe and bad_levels_allowed > 0:
            safe = any(self.is_safe(values[:i] + values[i + 1 :], bad_levels_allowed - 1) for i in range(len(values)))

        return safe

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        return sum(self.is_safe(int_list) for int_list in self.get_int_lines(self.input_file))

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        return sum(self.is_safe(int_list, 1) for int_list in self.get_int_lines(self.input_file))
