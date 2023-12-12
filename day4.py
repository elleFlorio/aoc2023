from collections import defaultdict
from utils import read_input

input_strings = read_input("day04.txt")
test = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


def get_winning_amount(card: str):
    numbers, winners = card[9:].split("|")
    numbers = set([int(num) for num in numbers.split(" ") if num != ""])
    winners = set([int(num) for num in winners.split(" ") if num != ""])

    match = numbers & winners
    return len(match)


def part_one(cards: list[str]):
    result = 0
    for card in cards:
        winning_amount = get_winning_amount(card)
        if winning_amount:
            result += 2 ** (winning_amount - 1)

    return result


def part_two(cards: list[str]):
    total_cards = len(cards)
    copies = defaultdict(int)
    for card_idx, card in enumerate(cards, start=1):
        copies_amount = copies[card_idx]
        total_cards += copies_amount
        total_copies = 1 + copies_amount
        winning_amount = get_winning_amount(card)
        for win in range(card_idx + 1, card_idx + winning_amount + 1):
            copies[win] += total_copies
        total_copies -= 1

    return total_cards


if __name__ == '__main__':
    print(part_one(input_strings))
    print(part_two(input_strings))
