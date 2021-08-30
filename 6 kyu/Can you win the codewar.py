def codewar_result(codewarrior, opponent):
    codewarrior = sorted(codewarrior)
    dict = {"win": 0, "draw": 0, "lose": 0}
    while codewarrior:
        temp = codewarrior[0]
        temp2 = max(opponent)
        flag = False
        for i in opponent:
            if temp > i:
                flag = True
                temp2 = min(temp2, i)
        if flag:
            codewarrior = codewarrior[1:]
            opponent.remove(temp2)
            dict["win"] += 1
        else:
            if max(codewarrior) > max(opponent):
                codewarrior.remove(max(codewarrior))
                opponent.remove(max(opponent))
                dict["win"] += 1
            elif temp == temp2:
                codewarrior = codewarrior[1:]
                opponent.remove(temp2)
                dict["draw"] += 1
            else:
                codewarrior = codewarrior[1:]
                opponent.remove(temp2)
                dict["lose"] += 1
    if dict["win"] > dict["lose"]:
        return 'Victory'
    elif dict["lose"] > dict["win"]:
        return "Defeat"
    return 'Stalemate'