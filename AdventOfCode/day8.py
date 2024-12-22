""" Advent of Code 2024 Day 2 """

import itertools
from AdventOfCode.utilities import get_character_lines_and_elements, in_bounds


def find_nodes(lines: list, elements: dict, repeat: bool = False) -> set:
    """Find the nodes in the grid."""
    nodes = set()

    for _, locs in elements.items():
        for pair in itertools.combinations(locs, 2):
            delta_x = pair[1][0] - pair[0][0]
            delta_y = pair[1][1] - pair[0][1]

            temps = [(pair[0][0] - delta_x, pair[0][1] - delta_y), (pair[1][0] + delta_x, pair[1][1] + delta_y)]

            while True:
                keep_going = False

                for temp in temps:
                    if in_bounds(lines, temp):
                        nodes.add(temp)
                        keep_going = repeat and True

                if not keep_going:
                    break

                temps = [(temps[0][0] - delta_x, temps[0][1] - delta_y), (temps[1][0] + delta_x, temps[1][1] + delta_y)]

    return nodes


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    lines, elements = get_character_lines_and_elements(input_file, r"[A-Za-z0-9]")
    return str(len(find_nodes(lines, elements)))


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    lines, elements = get_character_lines_and_elements(input_file, r"[A-Za-z0-9]")
    nodes = find_nodes(lines, elements, True)

    for _, points in elements.items():
        nodes.update(points)

    return str(len(nodes))
