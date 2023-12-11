from utils import read_input

input_strings = read_input("day02.txt")


def is_possible(game):
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    color = []
    cur_val = []

    for c in game:
        if c.isdigit():
            cur_val.append(c)
        elif c.isalpha():
            color.append(c)
            color_val = colors.get("".join(color))
            if color_val:
                if int("".join(cur_val)) > color_val:
                    return False
                color = []
                cur_val = []

    return True


def power_set(game):
    colors = {
        "red": -1,
        "green": -1,
        "blue": -1
    }

    parsed_color = []
    parsed_val = []

    for c in game:
        if c.isdigit():
            parsed_val.append(c)
        elif c.isalpha():
            parsed_color.append(c)
            cur_color = "".join(parsed_color)
            color_val = colors.get(cur_color)
            if color_val:
                cur_val = int("".join(parsed_val))
                if cur_val > color_val:
                    colors[cur_color] = cur_val

                parsed_color = []
                parsed_val = []

    return colors["red"] * colors["green"] * colors["blue"]


def part_one(games):
    val = 0
    for index, game in enumerate(games, start=1):
        if is_possible(game[8:]):
            val += index

    print(val)


def part_two(games):
    val = 0
    for game in games:
        val += power_set(game[8:])

    print(val)


if __name__ == '__main__':
    part_one(input_strings)
    part_two(input_strings)
