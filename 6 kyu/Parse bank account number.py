def parse_bank_account(bank_account):
    temp=[list(i) for i in bank_account[:-1].split("\n")]
    res=[]
    for i in range(0, len(temp[0]),3):
        if "_" not in "".join(temp[0][i:i+3]):
            res.append(4) if temp[1][i]=="|" else res.append(1)
        else:
            if temp[1][i]!="|":
                res.append(2) if temp[2][i+2]!="|" else res.append(3) if temp[1][i+1]=="_" else res.append(7)
            else:
                if temp[1][i+1]!="_":
                    res.append(0)
                else:
                    if temp[1][i+2]=="|":
                        res.append(8) if temp[2][i]=="|" else res.append(9)
                    else:
                        res.append(6) if temp[2][i]=="|" else res.append(5)
    return int("".join(str(i) for i in res))
    return 0