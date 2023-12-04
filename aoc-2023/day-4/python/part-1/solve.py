import re
from functools import total_ordering
from typing import  List, Tuple
from enum import Enum


def solve(file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        game_points = list(map(calculate_points_per_game, lines))

    return sum(game_points)
        

def calculate_points_per_game(line: str) -> int:
    game = line.split('|')
    nums = re.compile(r"(\d+)(?![^:]*:)")
    game = list(map(nums.findall, game))
    
    prize_nums = [int(x) for x in game[1] if x in game[0]]

    return 2 ** (len(prize_nums) - 1) if len(prize_nums) > 0 else 0

if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)