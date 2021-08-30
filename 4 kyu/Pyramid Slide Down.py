def longest_slide_down(pyramid):
    index=len(pyramid)-2
    while index>=0:
        for i in range(index+1):
            pyramid[index][i]=pyramid[index][i]+max(pyramid[index+1][i], pyramid[index+1][i+1])
        index-=1
    return pyramid[0][0]
        