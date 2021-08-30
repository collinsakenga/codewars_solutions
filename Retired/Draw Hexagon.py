def draw_hexagon(side):
    res=[]
    for i in range(side-1):
        res.append(" "*(side-1-i)+" ".join(["*"]*(side+i)))
    return "\n".join(res+[" ".join(["*"]*(side*2-1))]+res[::-1])