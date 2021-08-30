def score_hand(cards):
    #score of each card 
    dict_cards ={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    temp=cards.copy()
    total=0
    #check the score of cards
    for card in temp:
        total+=dict_cards[card] 
    if 'A' in temp:
        while True:
            # "A" can be 1 or 11, in order to get the max value, "A" increased by 10 if total<=11
            if total<=11:
                total+=10
            #if total>11 and "A" change from 1 to 11, total will be larger than 21, which fails
            if total+10>21:
                break
    return total