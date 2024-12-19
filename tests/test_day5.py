""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from AdventOfCode import day5

inputs_dir = os.path.join(os.getcwd(), "inputs", "day5")


class TestDay(unittest.TestCase):
    """Test cases for the given day."""

    def test_day5_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day5.part1(os.path.join(inputs_dir, "sample.txt")), "143")

    def test_day5_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day5.part1(os.path.join(inputs_dir, "input.txt")), "5452")

    def test_day5_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day5.part2(os.path.join(inputs_dir, "sample.txt")), "123")

    def test_day5_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day5.part2(os.path.join(inputs_dir, "input.txt")), "4598")


if __name__ == "__main__":
    unittest.main()
