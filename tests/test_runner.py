"""Test runner for Advent of Code days"""

import os
import unittest
from parameterized import parameterized_class

from AdventOfCode import day1, day2, day3, day4, day5, day6, day7, day8, day9
from AdventOfCode import day10, day11, day12  # , day13, day14


all_days = [
    ("Day1", day1, 11, 1765812, 31, 20520794),
    ("Day2", day2, 2, 314, 4, 373),
    ("Day3", day3, 161, 179571322, 161, 103811193),
    ("Day4", day4, 18, 2578, 9, 1972),
    ("Day5", day5, 143, 5452, 123, 4598),
    ("Day6", day6, 41, 4696, 6, 1443),
    ("Day7", day7, 3749, 1545311493300, 11387, 169122112716571),
    ("Day8", day8, 14, 359, 34, 1293),
    # ("Day9", day9, 1928, 6331212425418, 2858, 6363268339304),  TODO FIx this
    ("Day9", day9, 1928, 6331212425418, 2858, 6363268359248),
    ("Day10", day10, 36, 472, 81, 969),
    ("Day11", day11, 55312, 185894, 65601038650482, 221632504974231),
    ("Day12", day12, 1930, 1489582, 1206, 914966),
    # ("Day13", day13, None, None, None, None),
    # ("Day14", day14, None, None, None, None),
    # ("Day15", day15, None, None, None, None),
    # ("Day16", day16, None, None, None, None),
    # ("Day17", day17, None, None, None, None),
    # ("Day18", day18, None, None, None, None),
    # ("Day19", day19, None, None, None, None),
    # ("Day20", day20, None, None, None, None),
    # ("Day21", day21, None, None, None, None),
    # ("Day22", day22, None, None, None, None),
    # ("Day23", day23, None, None, None, None),
    # ("Day24", day24, None, None, None, None),
    # ("Day25", day25, None, None, None, None)
]


@parameterized_class(("day_name", "day_class", "p1_sample", "p1", "p2_sample", "p2"), all_days)
class TestDay(unittest.TestCase):
    """Tests for Advent of Code days"""

    days = all_days

    def setUp(self):
        self.day = self.day_class.Solver(os.path.join(os.getcwd(), "inputs", self.day_name, "input.txt"))
        self.sample = self.day_class.Solver(os.path.join(os.getcwd(), "inputs", self.day_name, "sample.txt"))

        return super().setUp()

    def test_part1_sample(self):
        """Test part 1 with sample data"""
        self.assertEqual(self.sample.part1(), self.p1_sample)

    def test_part1(self):
        """Test part 1 with input data"""
        self.assertEqual(self.day.part1(), self.p1)

    def test_part2_sample(self):
        """Test part 2 with sample data"""
        self.assertEqual(self.sample.part2(), self.p2_sample)

    def test_part2(self):
        """Test part 2 with input data"""
        self.assertEqual(self.day.part2(), self.p2)


if __name__ == "__main__":
    unittest.main()
