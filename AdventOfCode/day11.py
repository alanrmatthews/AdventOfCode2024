""" Advent of Code 2024 Day 2 """

import math
from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 10 solution."""

    def __init__(self, input_file: str):
        # Only one line so we can just work with the first one.
        g = self.get_int_lines(input_file)
        self.stones = next(g)
        self.total_blinks = 0
        self.blink_history = {}
        super().__init__(input_file)

    def part1(self) -> int:
        """Returns the solution for part 1 of the day."""
        return sum(self.get_number_of_stones(stone, 25) for stone in self.stones)

    def part2(self) -> int:
        """Returns the solution for part 2 of the day."""
        return sum(self.get_number_of_stones(stone, 75) for stone in self.stones)

    def get_number_of_stones(self, stone: int, blinks_left: int) -> int:
        """Returns the number of stones after the given number of blinks."""
        if stone not in self.blink_history or blinks_left not in self.blink_history[stone]:
            if stone not in self.blink_history:
                self.blink_history[stone] = {}

            if blinks_left == 0:
                self.blink_history[stone][blinks_left] = 1
            else:
                if stone == 0:
                    self.blink_history[stone][blinks_left] = self.get_number_of_stones(1, blinks_left - 1)
                else:
                    # Get the number of digits in the stone
                    digits = int(math.log10(stone)) + 1

                    if not digits & 1:
                        divisor = 10 ** (digits // 2)
                        lhs = self.get_number_of_stones(stone // divisor, blinks_left - 1)
                        rhs = self.get_number_of_stones(stone % divisor, blinks_left - 1)
                        self.blink_history[stone][blinks_left] = lhs + rhs
                    else:
                        self.blink_history[stone][blinks_left] = self.get_number_of_stones(stone * 2024, blinks_left - 1)

        return self.blink_history[stone][blinks_left]

    def blink(self):
        """Blink the stones."""
        self.total_blinks += 1
        print(f"Total blinks: {self.total_blinks}")
        new_stones = []

        seen = {}

        for stone in self.stones:
            if stone in seen:
                print(f"Stone already seen {stone}")
            else:
                seen[stone] = True

            if stone == 0:
                new_stones.append(1)
                continue

            # Get the number of digits in the stone
            digits = int(math.log10(stone)) + 1

            if not digits & 1:
                divisor = 10 ** (digits // 2)
                new_stones.append(stone // divisor)
                new_stones.append(stone % divisor)
                continue

            new_stones.append(stone * 2024)

        self.stones = new_stones
