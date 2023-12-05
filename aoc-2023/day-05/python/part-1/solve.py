import re
from functools import total_ordering
from typing import List, Tuple
from enum import Enum

Map = List[List[int]]


def solve(file: str) -> int:
    with open(file) as f:
        seeds, maps = parse_input(f.read())

    return get_lowest_location(seeds, maps)


def parse_input(content: str) -> Tuple[List[int], List[Map]]:
    nums = re.compile(r"(\d+)")
    lines = content.split("\n\n")

    almanac = [list(filter(lambda x: x, map(nums.findall, j)))
               for j in [i.split("\n") for i in lines]]
    seeds, maps = almanac[0][0], almanac[1:]

    return list(map(int, seeds)), [[list(map(int, j)) for j in i] for i in maps]


def get_lowest_location(seeds: List[int], maps: List[Map]) -> int:
    print(maps)
    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = maps
    locations = []

    for seed in seeds:
        soil = get_mapped_value(seed, seed_to_soil)
        fertilizer = get_mapped_value(soil, soil_to_fertilizer)
        water = get_mapped_value(fertilizer, fertilizer_to_water)
        light = get_mapped_value(water, water_to_light)
        temp = get_mapped_value(light, light_to_temperature)
        humidity = get_mapped_value(temp, temperature_to_humidity)
        location = get_mapped_value(humidity, humidity_to_location)

        locations.append(location)

    return min(locations)


def get_mapped_value(value: int, map: Map) -> int:
    map = sorted(map, key=lambda x: x[1])
    for mapping in map:
        dest_start, source_start, range_len = mapping
        if source_start <= value <= source_start + range_len:
            return dest_start + (value - source_start)

    return value


if __name__ == '__main__':
    solution = solve('input.txt')
    print("SOLUTION: ", solution)
