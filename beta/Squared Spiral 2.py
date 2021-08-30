def gen(n):
    table={(0, 0):0}
    x=y=count=direction=0
    repeat=1
    while count<n:
        inner=0
        while count<n and inner<repeat:
            if direction==0:
                x+=1
            elif direction==1:
                y+=1
            elif direction==2:
                x-=1
            elif direction==3:
                y-=1
            count+=1
            inner+=1
            table[(x, y)]=count
        inner=0
        direction=(direction+1)%4
        while count<n and inner<repeat:
            if direction==0:
                x+=1
            elif direction==1:
                y+=1
            elif direction==2:
                x-=1
            elif direction==3:
                y-=1
            count+=1
            inner+=1
            table[(x, y)]=count
        direction=(direction+1)%4
        repeat+=1
    return table
table=gen(100000)
def squared_spiral(x, y):
    return table[(x, y)]
