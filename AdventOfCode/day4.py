""" Advent of Code 2024 Day 2 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 4 class"""

    def check_direction(self, grid, x_in: int, y_in: int, direction: tuple, keyword: str) -> bool:
        """Follow the direction in the grid to see if we can match the word."""

        dx, dy = direction

        x = x_in + dx
        y = y_in + dy

        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False

        if grid[x][y] == keyword[0]:
            if len(keyword) == 1:
                return True
            return self.check_direction(grid, x, y, direction, keyword[1:])

        return False

    def check_corners(self, grid, x: int, y: int) -> bool:
        """Check the corners of the grid for a match."""
        front_slash = [grid[x - 1][y - 1], grid[x + 1][y + 1]]
        back_slash = [grid[x - 1][y + 1], grid[x + 1][y - 1]]
        return "M" in front_slash and "M" in back_slash and "S" in front_slash and "S" in back_slash

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        directions = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0)]
        keyword = "XMAS"
        grid = self.get_character_lines()

        matches = 0

        for x, row in enumerate(grid):
            for y, char in enumerate(row):
                if char == keyword[0]:
                    for direction in directions:
                        if self.check_direction(grid, x, y, direction, keyword[1:]):
                            matches += 1

        return matches

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        grid = self.get_character_lines()

        matches = 0

        for x, row in enumerate(grid):
            for y, char in enumerate(row):
                if char == "A" and x > 0 and y > 0 and x < len(grid) - 1 and y < len(grid[0]) - 1:
                    if self.check_corners(grid, x, y):
                        matches += 1

        return matches
