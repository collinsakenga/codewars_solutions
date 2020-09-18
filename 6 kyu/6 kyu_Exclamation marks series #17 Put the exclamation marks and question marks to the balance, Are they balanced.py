dict = {"!": 2, "?": 3}


def balance(left, right):
    return "Left" if sum(dict[i] for i in left) > sum(dict[i] for i in right) else "Right" if sum(dict[i] for i in left) < sum(dict[i] for i in right) else "Balance"
