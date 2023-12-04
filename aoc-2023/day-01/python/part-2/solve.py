import re
from typing import List


def solve(file: str) -> int:
    with open(file) as f:
        content = list(map(lambda x: x.strip(), f.readlines()))

        content = list(map(lambda x: helper(x), content))

        print(content)

    return sum(content)


def helper(line: str) -> int:
    # Define a dictionary to map words to numbers
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    nums = []
    curr_word = ""
    for i in range(0, len(line)):
        first_char = line[i]
        if first_char.isalpha():  # letter
            curr_word += first_char
        elif first_char.isdigit():  # number
            nums.append(first_char)
            continue
        else:  # other
            continue

        # 6 is the max len of the nums, so there's no need to iterate more than that
        for j in range(i + 1, i + 1 + 6):
            if j >= len(line):
                break

            second_char = line[j]

            if second_char.isalpha():  # letter
                curr_word += second_char

                if curr_word in word_to_number.keys():
                    nums.append(word_to_number[curr_word])
                    curr_word = ""
                    break

            else:  # other
                break

        curr_word = ""

        print(nums)

    return int(nums[0] + nums[-1])


if __name__ == "__main__":
    solve("input.txt")
