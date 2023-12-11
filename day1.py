from utils import read_input

input_strings = read_input("day01.txt")

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def substring(sub):
    cur = []
    result = []

    if len(sub) < 1:
        return result

    for c in sub:
        cur.append(c)
        curstr = "".join(cur)
        if curstr.isdigit():
            result.append(curstr)
            break

        num = numbers.get(curstr, "")
        if num:
            result.append(num)
            break

    nextvals = substring(sub[1:])
    return result + nextvals


if __name__ == '__main__':
    val = 0
    for string in input_strings:
        parsed = substring(string)
        to_add = int(parsed[0] + parsed[-1])
        val += to_add

    print(val)
