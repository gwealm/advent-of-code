import re
from typing import List
from math import sqrt, floor, ceil


def solve(file: str) -> int:
    with open(file) as f:
        race = list(map(lambda x: int("".join(re.findall(r"(\d+)", x))), f.readlines()))

    return get_wins(race)


def get_wins(race: List[int]) -> int:
    total_time, max_distance = race
    
    get_func_roots = lambda a, b, c: [ floor((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)), ceil((-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)) ]

    # The time function is:  f(x) = -x^2 + total_time * x - c 
    min_button_time, max_button_time = get_func_roots(-1, total_time, -max_distance)
    
    return max_button_time - min_button_time - 1    # we subtract 1, because the roots are not included


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)

