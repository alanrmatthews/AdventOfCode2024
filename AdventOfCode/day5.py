""" Advent of Code 2024 Day 2 """

from functools import cmp_to_key
from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 10 solution."""

    def parse_input(self, file: str) -> tuple:
        """Parses the input file and returns the orders and pages."""
        orders = []
        pages = []

        with open(file, "r", encoding="utf-8") as f:
            first_section = True

            for line in f:
                if line == "\n":
                    first_section = False
                elif first_section:
                    orders.append(list(map(int, line.strip().split("|"))))
                else:
                    pages.append(list(map(int, line.strip().split(","))))

        return orders, pages

    def validate_ordering(self, orders: list, page: list, part_one: bool = False) -> int:
        """Validates the ordering of the pages and returns the middle page if valid."""
        page_ordering_dict = {}
        for lhs, rhs in orders:
            if lhs in page and rhs in page:
                page_ordering_dict.setdefault(lhs, set()).add(rhs)
                page_ordering_dict.setdefault(rhs, set())

        page_ordering = list(page_ordering_dict.keys())
        page_ordering.sort(key=cmp_to_key(lambda x, y: -1 if y in page_ordering_dict[x] else (1 if x in page_ordering_dict[y] else 0)))

        if page_ordering == page:
            if part_one:
                return page[len(page) // 2]
            else:
                return 0
        else:
            if part_one:
                return 0
            else:
                return page_ordering[len(page_ordering) // 2]

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        ordering, pages = self.parse_input(self.input_file)
        return sum(self.validate_ordering(ordering, page, part_one=True) for page in pages)

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        ordering, pages = self.parse_input(self.input_file)
        return sum(self.validate_ordering(ordering, page, part_one=False) for page in pages)
