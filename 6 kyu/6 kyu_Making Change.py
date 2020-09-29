def make_change(amount):
    dict = {"H": 0, "Q": 0, "D": 0, "N": 0, "P": 0}
    add(dict, add(dict, add(dict, add(
        dict, add(dict, amount, 50, "H"), 25, "Q"), 10, "D"), 5, "N"), 1, "P")
    return {k: v for k, v in dict.items() if v > 0}


def add(dict, amount, dollar, sign):
    dict[sign] += amount//dollar
    amount -= amount//dollar*dollar
    return amount
