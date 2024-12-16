""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from src import day1

inputs_dir = os.path.join(os.getcwd(), "inputs", "day1")


class TestDay1(unittest.TestCase):
    """Test cases for the given day."""

    def test_day1_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day1.part1(os.path.join(inputs_dir, "sample.txt")), "11")

    def test_day1_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day1.part1(os.path.join(inputs_dir, "input.txt")), "1765812")

    def test_day1_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day1.part2(os.path.join(inputs_dir, "sample.txt")), "31")

    def test_day1_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day1.part2(os.path.join(inputs_dir, "input.txt")), "20520794")


if __name__ == "__main__":
    unittest.main()
