import random


def wait_for_enter():
    while input("Press Enter to continue") != "":
        pass


def roll_dices():
    return sum([random.randint(1, 6), random.randint(1, 6)])


def score_after_1st_round(score):
    if roll_dices() == 7:
        score //= 7
    elif roll_dices() == 11:
        score *= 11
    else:
        score += roll_dices()
    return score


def rules_implementation():
    player = 0
    pc = 0
    while True:
        print(f"""
            Player score: {player}
            PC score: {pc}
            """)
        wait_for_enter()
        if player == 0 and pc == 0:
            player += roll_dices()
            pc += roll_dices()
        elif player <= 2001 and pc <= 2001:
            player = score_after_1st_round(player)
            pc = score_after_1st_round(pc)
        else:
            if player >= 2001:
                return f"The winner is player! Score: {player}"
            else:
                return f"The winner is PC! Score: {pc}"


print(rules_implementation())
