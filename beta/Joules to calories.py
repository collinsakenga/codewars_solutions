def calories(string):
    res=string.split()
    return round(int(res[0])*[1, 1000][res[1]!="J"]/4.184)