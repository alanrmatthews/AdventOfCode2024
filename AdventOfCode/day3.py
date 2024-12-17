""" Advent of Code 2024 Day 2 """

import re


def parse_instructions(line: str, filtering: bool = False) -> int:
    """Parses the instructions from the line."""
    disabled_region = set()
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    if filtering:
        index = line.find("don't()")
        while index != -1:
            start = index
            end = line.find("do()", start)
            if end == -1:
                end = len(line)
            end += 1
            disabled_region.update(range(start, end))
            index = line.find("don't()", end)

    return sum(int(match.group(1)) * int(match.group(2)) for match in matches if match.start() not in disabled_region)


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    with open(input_file, encoding="utf-8") as file:
        lines = file.readlines()
        return str(parse_instructions(lines[0]))


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    with open(input_file, encoding="utf-8") as file:
        lines = file.readlines()
        return str(parse_instructions(lines[0], True))
