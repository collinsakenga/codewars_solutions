from itertools import product
def rolldice_sum_prob(sum_, dice_amount):
    if dice_amount*6<sum_ or sum_<dice_amount:
        return 0
    return sum(sum(i)==sum_ for i in product(list(range(1, 7)), repeat=dice_amount))/6**dice_amount