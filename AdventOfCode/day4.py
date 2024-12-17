""" Advent of Code 2024 Day 2 """


def check_direction(grid, x_in: int, y_in: int, direction: tuple, keyword: str) -> bool:
    """Follow the direction in the grid to see if we can match the word."""

    dx, dy = direction

    x = x_in + dx
    y = y_in + dy

    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False

    if grid[x][y] == keyword[0]:
        if len(keyword) == 1:
            return True
        return check_direction(grid, x, y, direction, keyword[1:])

    return False


def get_character_lines(input_file: str) -> list[list[chr]]:
    """Read the file at the given path and return a list of characters for each line in the file."""
    with open(input_file, encoding="utf-8") as file:
        return [list(line.strip()) for line in file]


def check_corners(grid, x: int, y: int) -> bool:
    """Check the corners of the grid for a match."""
    front_slash = [grid[x - 1][y - 1], grid[x + 1][y + 1]]
    back_slash = [grid[x - 1][y + 1], grid[x + 1][y - 1]]
    return "M" in front_slash and "M" in back_slash and "S" in front_slash and "S" in back_slash


def part1(input_file: str) -> str:
    """Returns the solution for part 1 of the day."""
    directions = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0)]
    keyword = "XMAS"
    grid = get_character_lines(input_file)

    matches = 0

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == keyword[0]:
                for direction in directions:
                    if check_direction(grid, x, y, direction, keyword[1:]):
                        matches += 1

    return str(matches)


def part2(input_file: str) -> str:
    """Returns the solution for part 2 of the day."""
    grid = get_character_lines(input_file)

    matches = 0

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == "A" and x > 0 and y > 0 and x < len(grid) - 1 and y < len(grid[0]) - 1:
                if check_corners(grid, x, y):
                    matches += 1

    return str(matches)
