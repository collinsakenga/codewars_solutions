left = {"w": 4, "p": 3, "b": 2, "s": 1}
right = {"m": 4, "q": 3, "d": 2, "z": 1}


def alphabet_war(fight):
    if len(fight) == 1:
        return "Left side wins!" if fight in "wpbs" else "Right side wins!" if fight in "mqdz" else "Let's fight again!"
    res = ""
    for i, j in enumerate(fight):
        if j == "*":
            continue
        if i == 0 and fight[i+1] != "*":
            res += j
        elif i == len(fight)-1 and fight[i-1] != "*":
            res += j
        elif fight[i-1] != "*" and fight[i+1] != "*":
            res += j
    left_total = 0
    right_total = 0
    for i in res:
        if left.get(i, None):
            left_total += left[i]
        elif right.get(i, None):
            right_total += right[i]
    return "Left side wins!" if left_total > right_total else "Right side wins!" if left_total < right_total else "Let's fight again!"
