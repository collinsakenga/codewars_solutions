def sqInRect(length, width):
    print(length, width)
    if length== width:
        return None
    square=min(length, width)
    result=[]
    while length!=0 and width !=0:
        if min(length, width)==square :
            result.append(square)
            if length>width:
                length-=square
            else:
                width-=square
        else:
            square-=1
    return result