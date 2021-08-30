def min_max(x,y):
    table={str(i):j for i,j in enumerate("zero one two three four five six seven eight nine".split())}
    left, right="".join(table[i] for i in str(x)), "".join(table[i] for i in str(y))
    return ord(max(left))+ord(min(right))