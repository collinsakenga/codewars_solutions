dict={'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
def krazy_king_blackjack (hand, king_value):
    res=sum(dict[i] for i in hand)
    if res<=11 and "A" in hand and "K" not in hand:
        res+=10
    res2=sum(dict[i] if i!="K" else king_value for i in hand)
    if res2<=11 and "A" in hand:
        res2+=10
    if res>21 and res2>21:
        return False
    return res if res2>21 else res2 if res>21 else max(res, res2)