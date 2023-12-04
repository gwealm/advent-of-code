import re
from typing import List, Tuple


def solve(file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = helper(lines)
        print(lines)

    return sum(lines)


def helper(lines: List[str]) -> List[int]:
    nums = re.compile(r"(\d+)")
    matches = [nums.finditer(line) for line in lines]

    # (line, initial_pos, length)
    res_nums = []
    for idx, match in enumerate(matches):
        for x in match:
            if has_adjacent_symbol(lines, (idx, x.span()[0], x.span()[1] - 1)):
                res_nums.append(int(x.group()))

    return res_nums


def has_adjacent_symbol(mx: List[str], coords: Tuple[int, int, int]):
    neighbors = get_neighbors(mx, coords)
    print(neighbors)

    return any(not char.isalpha() and not char.isdigit() and char != '.' for char in neighbors)


def get_neighbors(mx: List[str], coords: Tuple[int, int, int]) -> List[str]:
    UPPER_BOUND = LEFT_BOUND = 0
    LOWER_BOUND = len(mx) - 1
    RIGHT_BOUND = len(mx[0]) - 1

    neighbors = []

    def is_within_bounds(
        line, col): return line >= UPPER_BOUND and line <= LOWER_BOUND and col >= LEFT_BOUND and col <= RIGHT_BOUND

    target_line, target_col, target_size = coords
    print(coords)

    for col in range(target_col - 1, target_size + 2):
        # Upper Bound
        if is_within_bounds(target_line - 1, col):
            neighbors.append(mx[target_line - 1][col])

        if is_within_bounds(target_line, col):
            neighbors.append(mx[target_line][col])

        # Lower Bound
        if is_within_bounds(target_line + 1, col):
            neighbors.append(mx[target_line + 1][col])

    return neighbors


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
