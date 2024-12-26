""" Advent of Code 2024 Day 2 """

from AdventOfCode.utilities import get_character_lines_and_elements


class Day10:
    """Advent of Code 2024 Day 10 solution."""

    def __init__(self, input_file: str):
        self.lines, self.elements = get_character_lines_and_elements(input_file, r"\d")
        self.all_trails = {}
        self.directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        self.ascending = "0123456789"

    def part1(self) -> int:
        """Returns the solution for part 1 of the day."""
        total_score = 0
        for head in self.elements["0"]:
            # There may be multiple ways to get to the same endpoint, so find unique endpoints.
            total_score += len(set(trail[-1] for trail in self.get_trail_score(head, 0)))
        return total_score

    def part2(self) -> int:
        """Returns the solution for part 2 of the day."""
        return sum(len(self.get_trail_score(head, 0)) for head in self.elements["0"])

    def in_bounds(self, pos: tuple[int, int]) -> bool:
        """Returns True if the tuple is in bounds of the grid."""
        return 0 <= pos[0] < len(self.lines) and 0 <= pos[1] < len(self.lines[0])

    def get_trail_score(self, head: tuple[int, int], level: int) -> list:
        """Returns the score of the trail starting at the given head."""
        if head in self.all_trails:
            return self.all_trails[head]

        if level == 9:
            self.all_trails[head] = [[head]]
            return [[head]]

        scores = []

        for direction in self.directions:
            next_pos = (head[0] + direction[0], head[1] + direction[1])
            if not self.in_bounds(next_pos):
                continue

            if self.lines[next_pos[0]][next_pos[1]] == self.ascending[level + 1]:
                score = self.get_trail_score(next_pos, level + 1)
                for s in score:
                    if len(s) == 9 - level:
                        scores.append([head] + s)

        self.all_trails[head] = scores
        return scores
