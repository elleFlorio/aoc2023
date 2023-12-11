import math
from utils import read_input
from collections import deque

input_strings = read_input("day03.txt")
test = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

left = lambda c_idx: c_idx - 1 >= 0
up = lambda r_idx: r_idx - 1 >= 0
right = lambda c_idx: c_idx + 1 < (len(input_strings[0]))
down = lambda r_idx: r_idx + 1 < (len(input_strings))
top_left = lambda r_idx, c_idx: left(c_idx) and up(r_idx)
top_right = lambda r_idx, c_idx: right(c_idx) and up(r_idx)
bottom_left = lambda r_idx, c_idx: left(c_idx) and down(r_idx)
bottom_right = lambda r_idx, c_idx: right(c_idx) and down(r_idx)


def is_valid(row_idx, char_idx, schema):
    def is_symbol(c):
        return not (c.isdigit() or c == ".")

    if left(char_idx):
        to_check = schema[row_idx][char_idx - 1]
        if is_symbol(to_check):
            return True

    if up(row_idx):
        to_check = schema[row_idx - 1][char_idx]
        if is_symbol(to_check):
            return True

    if right(char_idx):
        to_check = schema[row_idx][char_idx + 1]
        if is_symbol(to_check):
            return True

    if down(row_idx):
        to_check = schema[row_idx + 1][char_idx]
        if is_symbol(to_check):
            return True

    if top_left(row_idx, char_idx):
        to_check = schema[row_idx - 1][char_idx - 1]
        if is_symbol(to_check):
            return True

    if top_right(row_idx, char_idx):
        to_check = schema[row_idx - 1][char_idx + 1]
        if is_symbol(to_check):
            return True

    if bottom_left(row_idx, char_idx):
        to_check = schema[row_idx + 1][char_idx - 1]
        if is_symbol(to_check):
            return True

    if bottom_right(row_idx, char_idx):
        to_check = schema[row_idx + 1][char_idx + 1]
        if is_symbol(to_check):
            return True

    return False


def part_one(schema):
    result = 0
    valid_numbers = []
    not_valid_numbers = []
    for row_idx, row in enumerate(schema):
        row_numbers = []
        not_valid_row_numbers = []
        parsed_num = []
        valid = False
        parsing_complete = False
        for char_idx, c in enumerate(row):
            if c.isdigit():
                parsed_num.append(c)
                if not valid:
                    valid = is_valid(row_idx, char_idx, schema)
                if char_idx == len(row) - 1:
                    parsing_complete = True
            else:
                parsing_complete = True

            if parsing_complete:
                if parsed_num:
                    if valid:
                        row_numbers.append(int("".join(parsed_num)))
                        result += int("".join(parsed_num))
                    else:
                        not_valid_row_numbers.append(int("".join(parsed_num)))

                    parsed_num = []
                    valid = False
                parsing_complete = False

        valid_numbers.append(row_numbers)
        not_valid_numbers.append(not_valid_row_numbers)

    print(result)


def check_surroundings(row_idx, char_idx, schema):
    left = lambda c_idx: c_idx - 1 >= 0
    up = lambda r_idx: r_idx - 1 >= 0
    right = lambda c_idx: c_idx + 1 < (len(schema[0]))
    down = lambda r_idx: r_idx + 1 < (len(schema))
    top_left = lambda r_idx, c_idx: left(c_idx) and up(r_idx)
    top_right = lambda r_idx, c_idx: right(c_idx) and up(r_idx)
    bottom_left = lambda r_idx, c_idx: left(c_idx) and down(r_idx)
    bottom_right = lambda r_idx, c_idx: right(c_idx) and down(r_idx)

    def parse_left(r_idx, c_idx):
        parsed = deque()
        while c_idx >= 0 and schema[r_idx][c_idx].isdigit():
            parsed.appendleft(schema[r_idx][c_idx])
            c_idx -= 1
        return parsed

    def parse_right(r_idx, c_idx):
        parsed = deque()
        while c_idx < len(schema[r_idx]) and schema[r_idx][c_idx].isdigit():
            parsed.append(schema[r_idx][c_idx])
            c_idx += 1
        return parsed

    numbers = [-1] * 8

    if left(char_idx):
        parsed_num = parse_left(row_idx, char_idx - 1)
        if parsed_num:
            numbers[0] = (int("".join(parsed_num)))
            parsed_num.clear()

    if right(char_idx):
        parsed_num = parse_right(row_idx, char_idx + 1)
        if parsed_num:
            numbers[1] = (int("".join(parsed_num)))
            parsed_num.clear()

    if up(row_idx):
        parsed_num = parse_left(row_idx - 1, char_idx)
        if parsed_num:
            parsed_num += parse_right(row_idx - 1, char_idx + 1)
            numbers[2] = (int("".join(parsed_num)))
            parsed_num.clear()

    if down(row_idx):
        parsed_num = parse_left(row_idx + 1, char_idx)
        if parsed_num:
            parsed_num += parse_right(row_idx + 1, char_idx + 1)
            numbers[3] = (int("".join(parsed_num)))
            parsed_num.clear()

    if top_left(row_idx, char_idx) and numbers[2] == -1:
        parsed_num = parse_left(row_idx - 1, char_idx - 1)
        if parsed_num:
            numbers[4] = (int("".join(parsed_num)))
            parsed_num.clear()

    if top_right(row_idx, char_idx) and numbers[2] == -1:
        parsed_num = parse_right(row_idx - 1, char_idx + 1)
        if parsed_num:
            numbers[5] = (int("".join(parsed_num)))
            parsed_num.clear()

    if bottom_left(row_idx, char_idx) and numbers[3] == -1:
        parsed_num = parse_left(row_idx + 1, char_idx - 1)
        if parsed_num:
            numbers[6] = (int("".join(parsed_num)))
            parsed_num.clear()

    if bottom_right(row_idx, char_idx) and numbers[3] == -1:
        parsed_num = parse_right(row_idx + 1, char_idx + 1)
        if parsed_num:
            numbers[7] = (int("".join(parsed_num)))
            parsed_num.clear()

    factors = [num for num in numbers if num > -1]
    if len(factors) > 1:
        return math.prod(factors)

    return 0


def part_two(schema):
    result = 0
    for row_idx, row in enumerate(schema):
        for char_idx, c in enumerate(row):
            if c == "*":
                result += check_surroundings(row_idx, char_idx, schema)

    print(result)


if __name__ == '__main__':
    part_one(input_strings)
    part_two(input_strings)
