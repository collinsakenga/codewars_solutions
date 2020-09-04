from collections import Counter
score = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


def get_score(dice):
    temp = sorted(Counter(dice).items(), key=lambda x: x[1])
    if len(temp) == 6:
        return 1000
    elif len(temp) == 3 and temp[0][1] == 2:
        return 750
    total = 0
    for i in temp:
        if i[1] >= 3:
            total += (i[1]-2)*score[i[0]]
        elif i[0] == 1 or i[0] == 5:
            total += 100*i[1] if i[0] == 1 else 50*i[1]
    return "Zonk" if not total else total
