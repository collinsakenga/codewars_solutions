dict={'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
def winner(deck_steve, deck_josh):
    res=[1 if dict[deck_steve[i]]>dict[deck_josh[i]] else 2 if dict[deck_josh[i]]>dict[deck_steve[i]] else 0 for i in range(len(deck_steve))]
    return f"Steve wins {res.count(1)} to {res.count(2)}" if res.count(1)>res.count(2) else f"Josh wins {res.count(2)} to {res.count(1)}" if res.count(2)>res.count(1) else "Tie"