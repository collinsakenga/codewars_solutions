def data_reverse(data):
    res=[data[i:i+8] for i in range(0,len(data), 8)]
    res.reverse()
    return [j for i in res for j in i]
    