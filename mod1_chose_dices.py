import random

POSSIBLE_DICES = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def valid_dices(chosen_dice):
    for dice in POSSIBLE_DICES:
        if dice == chosen_dice:
            return chosen_dice[1:]


def chose_dice(dices_amount):
    dices = []
    for dice_nr in range(1, dices_amount + 1):
        while True:
            try:
                choice = input(f"Chose dice nr {dice_nr}: ")
                dices.append(int(valid_dices(choice)))
                break
            except TypeError:
                print("Wrong input")
    return dices


def roll_dice(sides):
    return random.randint(1, sides)


def game(dices_amount):
    for sides in chose_dice(dices_amount):
        (roll_dice(sides))



