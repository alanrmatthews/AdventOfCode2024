""" Advent of Code 2024 Day 2 """

from AdventOfCode.day_base import AdventOfCodeDay


class Solver(AdventOfCodeDay):
    """Advent of Code 2024 Day 10 solution."""

    def build_fs(self, line: str) -> list:
        """Returns a list of tuples with the following format: index, count, spaces"""
        fs = []
        ptr = 0
        val = 0

        while True:
            if ptr >= len(line) - 1:
                fs.append((val, int(line[ptr]), 0))
                return fs

            fs.append((val, int(line[ptr]), int(line[ptr + 1])))

            ptr += 2
            val += 1

    def compact_fs(self, fs: list) -> list:
        out = []

        f_val, f_count, spaces = fs.pop(0)
        b_val, b_count, _ = fs.pop(-1)

        while fs:
            out += [f_val] * f_count

            while spaces > 0:
                temp = min(spaces, b_count)
                out += [b_val] * temp
                spaces -= temp
                b_count -= temp

                if b_count == 0:
                    b_val, b_count, _ = fs.pop(-1)

            if fs:
                f_val, f_count, spaces = fs.pop(0)
            else:
                out += [b_val] * b_count
                return out

        # There could be remaining counts, add them here
        out += [f_val] * f_count
        out += [b_val] * b_count
        return out

    def find_block(self, fs: list, spaces: int) -> int:
        if spaces == 0:
            return None

        for idx, i in enumerate(reversed(fs)):
            if i[1] <= spaces and i[0] is not None:
                return len(fs) - idx - 1

        return None

    def compact_fs_no_split(self, fs: list) -> list:
        out = []

        while fs:
            f_val, f_count, spaces = fs.pop(0)
            out += [f_val] * f_count

            block = self.find_block(fs, spaces)
            while block:
                v, c, s = fs[block]
                fs[block] = (None, c, s)
                out += [v] * c
                spaces -= c
                block = self.find_block(fs, spaces)
            out += [None] * spaces

        return out

    def part1(self) -> str:
        """Returns the solution for part 1 of the day."""
        with open(self.input_file, "r", encoding="utf-8") as file:
            line = file.readline()

        fs = self.build_fs(line)

        return sum(idx * val for idx, val in enumerate(self.compact_fs(fs)))

    def part2(self) -> str:
        """Returns the solution for part 2 of the day."""
        with open(self.input_file, "r", encoding="utf-8") as file:
            line = file.readline()

        fs = self.build_fs(line)

        return sum(idx * val for idx, val in enumerate(self.compact_fs_no_split(fs)) if val is not None)
