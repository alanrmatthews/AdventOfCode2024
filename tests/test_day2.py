""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from AdventOfCode import day2

inputs_dir = os.path.join(os.getcwd(), "inputs", "day2")


class TestDay2(unittest.TestCase):
    """Test cases for the given day."""

    def test_day2_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day2.part1(os.path.join(inputs_dir, "sample.txt")), "2")

    def test_day2_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day2.part1(os.path.join(inputs_dir, "input.txt")), "314")

    def test_day2_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day2.part2(os.path.join(inputs_dir, "sample.txt")), "4")

    def test_day2_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day2.part2(os.path.join(inputs_dir, "input.txt")), "373")


if __name__ == "__main__":
    unittest.main()
