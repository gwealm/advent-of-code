import re
from typing import List, Tuple

Map = List[List[int]]


def solve(file: str) -> int:
    with open(file) as f:
        seeds, maps = parse_input(f.read())

    return reverse_lookup(seeds, maps)


def parse_input(content: str) -> Tuple[List[int], List[Map]]:
    nums = re.compile(r"(\d+)")
    lines = content.split("\n\n")

    almanac = [list(filter(lambda x: x, map(nums.findall, j)))
               for j in [i.split("\n") for i in lines]]
    seeds, maps = list(map(int, almanac[0][0])), [
        [list(map(int, j)) for j in i] for i in almanac[1:]]

    return seeds, maps


def seed_exists(seed: int, seeds: List[int]) -> bool:
    for i in range(0, len(seeds), 2):
        if seeds[i] <= seed < seeds[i] + seeds[i + 1]:
            return True

    return False


def reverse_lookup(seeds: List[int], maps: List[Map]) -> int:
    location = 0

    while True:
        seed = get_seed(location, maps)
        if seed_exists(seed, seeds):
            return location

        location += 1


def get_seed(location: int, maps: List[Map]):
    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = maps

    humidity = get_reversed_mapped_value(location, humidity_to_location)
    temp = get_reversed_mapped_value(humidity, temperature_to_humidity)
    light = get_reversed_mapped_value(temp, light_to_temperature)
    water = get_reversed_mapped_value(light, water_to_light)
    fertilizer = get_reversed_mapped_value(water, fertilizer_to_water)
    soil = get_reversed_mapped_value(fertilizer, soil_to_fertilizer)
    seed = get_reversed_mapped_value(soil, seed_to_soil)

    return seed


def get_reversed_mapped_value(dest_value: int, map: Map) -> int:
    map = sorted(map, key=lambda x: x[0])
    for mapping in map:
        dest_start, source_start, range_len = mapping
        if dest_start <= dest_value < dest_start + range_len:

            return source_start + (dest_value - dest_start)

    return dest_value


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
