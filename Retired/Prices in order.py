# Each of the variables is an integer for the price of the drink
def areDrinkPricesCorrect(small, medium, big):
    return small==min(small, medium, big) and big==max(small, medium, big)