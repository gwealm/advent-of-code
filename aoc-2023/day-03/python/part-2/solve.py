import re
from typing import  List, Tuple, Dict
from functools import reduce


def solve(file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        gear_ratio = helper(lines)


    return gear_ratio
        

def helper(lines: List[str]) -> int:
    nums = re.compile(r"(\d+)")
    matches = [nums.finditer(line) for line in lines]

    """
    (line, initial_pos, length)
    """
    gear_ratio = dict()
    for idx, match in enumerate(matches):
        for x in match:
            get_neighbor_gears(lines, (idx, x.span()[0], x.span()[1]), gear_ratio, int(x.group()))
            print(gear_ratio)
            ratio = calculate_gear_ratio(gear_ratio)
            
            
    return ratio
    

def neighbors_helper(line: int, col: int):
    return [
        (line - 1, col - 1), (line, col - 1), (line + 1, col - 1),
        (line - 1, col), (line + 1, col),
        (line - 1, col + 1), (line, col + 1), (line + 1, col + 1)
    ]
    
def calculate_gear_ratio(gear: Dict[Tuple[int, int], List[int]]) -> int:
    ratios = []
    for el in gear.values():
        if len(el) > 1:     # don«t multiply elements without 2 gears
            ratios.append(reduce(lambda a, b: a * b, el))
        
    return sum(ratios)
    

def get_neighbor_gears(mx: List[str], coords: Tuple[int, int, int], dict: Dict[Tuple[int, int], List[int]], num: int) -> List[str] :
    UPPER_BOUND = LEFT_BOUND = 0
    LOWER_BOUND = len(mx) - 1
    RIGHT_BOUND = len(mx[0]) - 1
    
    neighbors = []
    
    is_within_bounds = lambda line, col: line >= UPPER_BOUND and line <= LOWER_BOUND and col >= LEFT_BOUND and col <= RIGHT_BOUND
    
    target_line, target_col, target_size = coords
    print (coords)

    visited_list = []
    
    for col in range(target_col, target_size):

        for n_line, n_col in neighbors_helper(target_line, col):
            if is_within_bounds(n_line, n_col):
                if mx[n_line][n_col] == '*':
                    if (n_line, n_col) in visited_list:
                        continue
                    
                    visited_list.append((n_line, n_col))
                    updated_list = dict.get((n_line, n_col), []) + [num]
                    dict.update({(n_line, n_col): updated_list})
    
    return neighbors



        
if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)