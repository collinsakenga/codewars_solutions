def get_most_profit_from_stock_quotes(quotes): 
    index=quotes.index(max(quotes))
    start=-1
    total=0
    while index<len(quotes):
        total+=quotes[index]*(index-start-1)-sum(quotes[start+1:index])
        start=index
        if index==len(quotes)-1:
            index+=1
        else:
            index+=quotes[index+1:].index(max(quotes[index+1:]))+1
    return total