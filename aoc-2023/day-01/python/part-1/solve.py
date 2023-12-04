import re
from typing import List


def solve(file: str) -> List[int]:
    with open(file) as f:
        content = list(map(lambda x: x.strip(), f.readlines()))

        num_list = list(map(lambda x: re.findall(r'\d', x), content))

        num_list = list(map(lambda x: int(x[0] + x[-1]), num_list))

    return num_list


if __name__ == "__main__":
    print(solve("input.txt"))
