""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from AdventOfCode import day3

inputs_dir = os.path.join(os.getcwd(), "inputs", "day3")


class TestDay3(unittest.TestCase):
    """Test cases for the given day."""

    def test_day3_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day3.part1(os.path.join(inputs_dir, "sample.txt")), "161")

    def test_day3_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day3.part1(os.path.join(inputs_dir, "input.txt")), "179571322")

    def test_day3_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day3.part2(os.path.join(inputs_dir, "sample2.txt")), "48")

    def test_day3_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day3.part2(os.path.join(inputs_dir, "input.txt")), "103811193")


if __name__ == "__main__":
    unittest.main()
