""" Unit tests for the specified days' module of AdventOfCode2024. """

import cProfile
import unittest
import os

from AdventOfCode import day11

inputs_dir = os.path.join(os.getcwd(), "inputs", "day11")


class TestDay(unittest.TestCase):
    """Test cases for the given day."""

    day_sample = day11.Day11(os.path.join(inputs_dir, "sample.txt"))
    day = day11.Day11(os.path.join(inputs_dir, "input.txt"))

    def test_day11_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(self.day_sample.part1(), 55312)

    def test_day11_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(self.day.part1(), 185894)

    def test_day11_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        # There's no test for part2 in the sample file.

    def test_day11_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(self.day.part2(), 221632504974231)


if __name__ == "__main__":
    unittest.main()
