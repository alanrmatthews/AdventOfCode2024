""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from AdventOfCode import day4

inputs_dir = os.path.join(os.getcwd(), "inputs", "day4")


class TestDay4(unittest.TestCase):
    """Test cases for the given day."""

    def test_day4_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day4.part1(os.path.join(inputs_dir, "sample.txt")), "18")

    def test_day4_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day4.part1(os.path.join(inputs_dir, "input.txt")), "2578")

    def test_day4_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day4.part2(os.path.join(inputs_dir, "sample.txt")), "9")

    def test_day4_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day4.part2(os.path.join(inputs_dir, "input.txt")), "1972")


if __name__ == "__main__":
    unittest.main()
