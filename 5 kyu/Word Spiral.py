def spiralize(word):
    table={}
    y=x=0
    directions=((1, 0), (0, 1), (-1, 0), (0, -1))
    for i,j in enumerate(word):
        dy, dx=directions[i%4]
        for k in range(ord(j)-ord("a")+1):
            y+=dy
            x+=dx
            table[(y, x)]=j
    left, right=min(i[1] for i in table.keys()), max(i[1] for i in table.keys())+1
    up, down=min(i[0] for i in table.keys()), max(i[0] for i in table.keys())+1
    return "\n".join("".join(table.get((i, j), " ") for j in range(left, right)) for i in range(up, down))