def validate_bet(game, text):
    res=[]
    temp=""
    for i in text:
        if not ( i=="," or i==" " or i.isdigit()):
            return None
        if i.isdigit():
            temp+=i
        else:
            if temp: res.append(int(temp)) 
            temp=""
    if temp: res.append(int(temp))
    if len(set(res))!=game[0] or max(res)>game[1]: return None
    return sorted(res) if len(res)==game[0] and 0 not in res else None