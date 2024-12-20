""" Unit tests for the specified days' module of AdventOfCode2024. """

import unittest
import os
from AdventOfCode import day7

inputs_dir = os.path.join(os.getcwd(), "inputs", "day7")


class TestDay(unittest.TestCase):
    """Test cases for the given day."""

    def test_day7_part1_sample(self):
        """Test the part1 function of days' module with a sample input file."""
        self.assertEqual(day7.part1(os.path.join(inputs_dir, "sample.txt")), "3749")

    def test_day7_part1(self):
        """Test the part1 function of days' module with the real input file."""
        self.assertEqual(day7.part1(os.path.join(inputs_dir, "input.txt")), "1545311493300")

    def test_day7_part2_sample(self):
        """Test the part2 function of days' module with a sample input file."""
        self.assertEqual(day7.part2(os.path.join(inputs_dir, "sample.txt")), "11387")

    def test_day7_part2(self):
        """Test the part2 function of days' module with the real input file."""
        self.assertEqual(day7.part2(os.path.join(inputs_dir, "input.txt")), "169122112716571")


if __name__ == "__main__":
    unittest.main()
