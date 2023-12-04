import re
from functools import total_ordering
from typing import List, NamedTuple
from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


@total_ordering
class Cube(NamedTuple):
    red: int
    green: int
    blue: int

    def __repr__(self) -> str:
        return (f"Cube({Color.RED.value}:{self.red}, {Color.GREEN.value}: {self.green}, {Color.BLUE.value}:{self.blue})")

    def _is_valid_operand(self, other):
        return (hasattr(other, Color.RED.value) and hasattr(other, Color.GREEN.value) and hasattr(other, Color.BLUE.value))

    def __eq__(self, other) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.red == other.red and self.green == other.green and self.blue == other.blue)

    def __lt__(self, other) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.red < other.red and self.green < other.green and self.blue < other.blue)

    def __le__(self, other) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.red <= other.red and self.green <= other.green and self.blue <= other.blue)

    def __gt__(self, other) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.red > other.red or self.green > other.green or self.blue > other.blue)


Game = List[Cube]
GameCollection = List[Game]


def solve(file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        data = list(map(format_data, lines))

        min_cubes = get_min_cubes(data)

        return sum(map(lambda x: x.red * x.green * x.blue, min_cubes))


def format_data(line: str) -> Game:
    game_sets = line.split(";")
    rgb_re = re.compile(r"\b(\d+)\s(red|green|blue)\b", re.IGNORECASE)

    game = list(map(rgb_re.findall, game_sets))

    game = map(lambda x: {play[1]: int(play[0]) for play in x}, game)
    game = [Cube(entry.get(Color.RED.value, 0), entry.get(
        Color.GREEN.value, 0), entry.get(Color.BLUE.value, 0)) for entry in game]

    return game


def get_min_cubes(data: GameCollection) -> List[Cube]:
    min_cubes = []

    for curr_game in data:
        r = max([cube.red for cube in curr_game])
        g = max([cube.green for cube in curr_game])
        b = max([cube.blue for cube in curr_game])

        min_cubes.append(Cube(r, g, b))

    return min_cubes


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
