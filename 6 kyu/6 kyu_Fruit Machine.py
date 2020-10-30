dict = {'Wild': 100, 'Star': 90, 'Bell': 80, 'Shell': 70, 'Seven': 60,
        'Cherry': 50, 'Bar': 40, 'King': 30, 'Queen': 20, 'Jack': 10}


def fruit(reels, spins):
    res = [items[index] for items, index in zip(reels, spins)]
    if len(set(res)) == 1:
        return dict[res[0]]
    elif len(set(res)) == 2:
        for i in set(res):
            if res.count(i) > 1:
                return 10 if i == "Wild" else dict[i]//10 if "Wild" not in res else dict[i]//10*2
    return 0