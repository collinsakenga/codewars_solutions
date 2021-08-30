def electrons_around_the_cores(dice):
    return sum(2 if i==3 else 4 if i==5 else 0 for i in dice)