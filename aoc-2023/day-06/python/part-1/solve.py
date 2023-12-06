import re
from typing import List
from functools import reduce


def solve(file: str):
    with open(file) as f:
        races = list(zip(*map(lambda x: re.findall(r"(\d+)", x), f.readlines())))
        races = [list(map(int, i)) for i in races]

    return reduce(lambda x, y: x * y, [get_wins_per_game(race) for race in races])


def get_wins_per_game(race: List[int]) -> int:
    total_time, max_distance = race
    winning_ways = 0

    # we can remove both edge cases since they both do 0 mm
    for button_time in range(1, total_time):

        distance = button_time * (total_time - button_time)

        if distance > max_distance:
            winning_ways += 1

    return winning_ways


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
