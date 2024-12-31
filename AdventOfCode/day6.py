""" Advent of Code 2024 Day 2 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 10 solution."""

    def get_starting_position(self, lines: list, character: str) -> tuple:
        """Returns the starting position of the character."""
        for x, line in enumerate(lines):
            for y, char in enumerate(line):
                if char == character:
                    return x, y

        return -1, -1

    def traverse_path(self, lines: list, row: int, col: int, obstacle_row: int = -1, obstacle_col: int = -1) -> tuple:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        current_direction = 0
        path = set()
        obstacles_seen = {0: set(), 1: set(), 2: set(), 3: set()}
        is_infinite = False

        while 0 <= row < len(lines) and 0 <= col < len(lines[0]):
            if lines[row][col] == "#" or row == obstacle_row and col == obstacle_col:
                if (row, col) in obstacles_seen[current_direction]:
                    is_infinite = True
                    break
                obstacles_seen[current_direction].add((row, col))
                row -= directions[current_direction][0]
                col -= directions[current_direction][1]
                current_direction = (current_direction + 1) % 4
            else:
                path.add((row, col))

            row += directions[current_direction][0]
            col += directions[current_direction][1]

        return path, is_infinite

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        lines = self.get_character_lines()
        row, col = self.get_starting_position(lines, "^")

        return len(self.traverse_path(lines, row, col)[0])

    # TODO Too slow, we should be able to figure out where obstacles could go during a single traverse.
    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        lines = self.get_character_lines()
        row, col = self.get_starting_position(lines, "^")

        path = self.traverse_path(lines, row, col)[0]
        path.remove((row, col))

        return sum(1 for x, y in path if self.traverse_path(lines, row, col, x, y)[1])
