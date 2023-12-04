import re
from typing import List, Tuple

cache = dict()

Game = List[List[int]]


def solve(file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
        games = [parse_game(line.strip()) for line in lines]

        # Pre-Cache game results to increase lookup efficiency
        for id, game in games:
            cache[id] = get_num_winners(game)

        game_points = get_total_tickets_num(games)

    return game_points


def get_total_tickets_num(games: List[Tuple[int, Game]]) -> int:
    return sum(helper(i) for i in cache.keys())


def helper(id) -> int:
    if id > len(cache):
        return 0

    return 1 + sum(helper(i) for i in range(id + 1, id + 1 + cache[id]))


def parse_game(line: str) -> Tuple[int, Game]:
    id = int(re.search(r"\d+", line).group())

    game = line.split('|')
    nums = re.compile(r"(\d+)(?![^:]*:)")
    game = list(map(nums.findall, game))

    return (id, game)


def get_num_winners(game: Game) -> int:
    prize_nums = [int(x) for x in game[1] if x in game[0]]

    return len(prize_nums)


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
