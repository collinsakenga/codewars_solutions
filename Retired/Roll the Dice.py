import random

def roll_the_dices(number_of_dices):
    if not isinstance(number_of_dices, int) or number_of_dices<=0:
        return False
    return [random.randint(1, 6) for i in range(number_of_dices)]