def sort_the_pile(pile_of_towels, weekly_used_towels):
    res=pile_of_towels[:]
    for week in weekly_used_towels:
        arr=[res.pop() for day in range(week)]
        arr.sort(key=lambda x: (0, 1)[x=="blue"])
        res.extend(arr)
    return res