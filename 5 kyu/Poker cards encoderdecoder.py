from itertools import product
def gen():
    count=0
    remain=0
    table={}
    for i in product("A23456789TJQK", "cdhs"):
        count=(count+1)%4
        table["".join(i)]=(count-1)%4*13+remain
        if count==0:
            remain+=1
    return table
table=gen()
table_reverse={j:i for i,j in table.items()}
def encode(cards):
    return sorted(table[i] for i in cards)

def decode(cards):
    return [table_reverse[i] for i in sorted(cards)]