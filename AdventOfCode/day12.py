""" Advent of Code 2024 Day 2 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day solution."""

    def __init__(self, input_file: str):
        super().__init__(input_file)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.grid = self.get_character_lines()
        self.regions = set()
        self.grid_processed = False

    def process_grid(self):
        """Processes the grid."""
        visited = set()

        for row, line in enumerate(self.grid):
            for col, _ in enumerate(line):
                node = (row, col)
                if node not in visited:
                    self.map_regions(visited, self.regions, node, None)

        self.grid_processed = True

    def map_regions(self, visited, regions, node, my_region):
        """Maps the regions in the grid."""

        visited.add(node)

        if my_region is None:
            my_region = self.Region(self.directions)
            regions.add(my_region)

        my_region.add_node(node, self.grid[node[0]][node[1]])

        matching_directions = []

        for idx, direction in enumerate(self.directions):
            new_node = (node[0] + direction[0], node[1] + direction[1])

            if 0 <= new_node[0] < len(self.grid) and 0 <= new_node[1] < len(self.grid[0]):
                if self.grid[new_node[0]][new_node[1]] == self.grid[node[0]][node[1]]:
                    matching_directions.append(idx)
                    if new_node not in visited:
                        self.map_regions(visited, regions, new_node, my_region)

        # Add perimeter to region (Part 1)
        my_region.add_perimeter(4 - len(matching_directions))
        my_region.node_directions[node] = matching_directions

    def part1(self) -> int:
        """Returns the solution for part 1 of the day."""
        if not self.grid_processed:
            self.process_grid()
        return sum(region.get_price() for region in self.regions)

    def part2(self) -> int:
        """Returns the solution for part 2 of the day."""
        if not self.grid_processed:
            self.process_grid()

        with open("output.txt", "w") as f:
            for region in self.regions:
                plant = region.value
                area = len(region.nodes)
                edges = region.sides
                f.write(f"{plant} (area: {area}, edges: {edges}): {sorted(region.nodes)}\n")

        return sum(region.get_discount_price() for region in self.regions)

    class Region:
        """Region class."""

        def __init__(self, directions: list):
            self.nodes = []
            self.perimeter = 0
            self.sides = 0
            self.edges = 0
            self.value = None
            self.directions = directions
            self.node_directions = {}

        def add_node(self, node, value):
            """Adds a node to the region."""
            if self.value is None:
                self.value = value
            else:
                assert self.value == value
            self.nodes.append(node)

        def add_perimeter(self, perimeter):
            """Adds a perimeter to the region."""
            self.perimeter += perimeter

        def num_sides(self):
            """Returns the number of sides in the region."""
            if self.sides == 0:
                self.sides = sum(self.get_num_corners(node) for node in self.nodes)

            return self.sides

        def get_price(self):
            """Returns the price of the region."""
            return self.perimeter * len(self.nodes)

        def get_discount_price(self):
            """Returns the discounted (part 2) price of the region."""
            return self.num_sides() * len(self.nodes)

        def get_diagonal_node(self, node: tuple, directions: list) -> tuple:
            """Returns the diagonal node based on directions."""
            d1 = self.directions[directions[0]]
            d2 = self.directions[directions[1]]

            return (node[0] + d1[0] + d2[0], node[1] + d1[1] + d2[1])

        def get_num_corners(self, node: tuple) -> int:
            """Returns the number of corners in a node based on neighbors."""
            directions = self.node_directions[node]

            match len(directions):
                case 0:
                    corners = 4
                case 1:
                    corners = 2
                case 2:
                    if directions not in [[1, 3], [0, 2]]:
                        diagonal = self.get_diagonal_node(node, directions)
                        if diagonal in self.nodes:
                            corners = 1
                        else:
                            corners = 2
                    else:
                        corners = 0
                case 3:
                    if 0 in directions and 2 in directions:
                        if 1 in directions:
                            corners = sum(1 for d in [[0, 1], [2, 1]] if self.get_diagonal_node(node, d) not in self.nodes)
                        else:
                            corners = sum(1 for d in [[0, 3], [2, 3]] if self.get_diagonal_node(node, d) not in self.nodes)
                    else:
                        if 0 in directions:
                            corners = sum(1 for d in [[0, 1], [0, 3]] if self.get_diagonal_node(node, d) not in self.nodes)
                        else:
                            corners = sum(1 for d in [[1, 2], [2, 3]] if self.get_diagonal_node(node, d) not in self.nodes)
                case 4:
                    corners = sum(1 for d in [[0, 1], [0, 3], [1, 2], [2, 3]] if self.get_diagonal_node(node, d) not in self.nodes)

            return corners
