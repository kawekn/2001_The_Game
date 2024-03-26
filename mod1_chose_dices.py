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


def chose_dices(dices_amount, player=0):
    dices = []
    for dice_nr in range(1, dices_amount + 1):
        if player == 0:
            choice = random.choice(POSSIBLE_DICES)
            dices.append(int(valid_dices(choice)))
        else:
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


def roll_dices(dices_amount, player, result=0,):
    for sides in chose_dices(dices_amount, player):
        result += (roll_dice(sides))
    return result


def score_after_1st_round(score, dices_amount, player):
    if roll_dices(dices_amount, player, score) == 7:
        score //= 7
    elif roll_dices(dices_amount, player, score) == 11:
        score *= 11
    else:
        score += roll_dices(dices_amount, player,score)
    return score


def rules_implementation(player_score=0, pc_score=0):
    while True:
        print(f"""
        Player score: {player_score}
            PC score: {pc_score}
        """)
        if player_score == 0 and pc_score == 0:
            player_score = roll_dices(2, 1)
            pc_score = roll_dices(2, 0)
        elif player_score <= 2001 and pc_score <= 2001:
            player_score = roll_dices(2, 1, player_score)
            pc_score = roll_dices(2, 0,pc_score)
        else:
            if player_score >= 2001:
                return f"The winner is player! Score: {player_score}"
            else:
                return f"The winner is PC! Score: {pc_score}"


print(rules_implementation())
