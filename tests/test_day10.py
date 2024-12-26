""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os

from AdventOfCode import day10

inputs_dir = os.path.join(os.getcwd(), "inputs", "day10")


class TestDay(unittest.TestCase):
    """Test cases for the given day."""

    day_sample = day10.Day10(os.path.join(inputs_dir, "sample.txt"))
    day = day10.Day10(os.path.join(inputs_dir, "input.txt"))

    def test_day10_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(self.day_sample.part1(), 36)

    def test_day10_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(self.day.part1(), 472)

    def test_day10_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(self.day_sample.part2(), 81)

    def test_day10_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(self.day.part2(), 969)


if __name__ == "__main__":
    unittest.main()
