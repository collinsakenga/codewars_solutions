def super_street_fighter_selection(fighters, position, moves):
    if not fighters[position[0]][position[1]]:
        return []
    res=[]
    row=position[0]
    col=position[1]
    for i in moves:
        if i=="up" and row==0:
            pass
        elif i=="up" and fighters[row-1][col]=="":
            pass
        elif i=="up":
            row-=1
        if i=="down" and row==len(fighters)-1:
            pass
        elif i=="down" and fighters[row+1][col]=="":
            pass
        elif i=="down":
            row+=1
        if i=="left" and col==0:
            col=len(fighters[0])-1
            while fighters[row][col]=="":
                col-=1
        elif i=="left" and fighters[row][col-1]=="":
            col-=1
            while fighters[row][col]=="":
                if col==0:
                    col=len(fighters[0])-1
                else:
                    col-=1
        elif i=="left":
            col-=1
        if i=="right" and col==len(fighters[0])-1:
            col=0
            while fighters[row][col]=="":
                col+=1
        elif i=="right" and fighters[row][col+1]=="":
            col+=1
            while fighters[row][col]=="":
                if col==len(fighters[0])-1:
                    col=0
                else:
                    col+=1
        elif i=="right":
            col+=1
        res.append(fighters[row][col])
    return res