def men_still_standing(cards):
    left=right=11
    arr1=[[True, 0] for i in range(11)]
    arr2=[[True, 0] for i in range(11)]
    for i in cards:
        if left<7 or right<7:
            break
        if i[0]=="A" and arr1[int(i[1:-1])-1][0]:
            if i[-1]=="R":
                arr1[int(i[1:-1])-1][0]=False
                left-=1
            elif i[-1]=="Y":
                arr1[int(i[1:-1])-1][1]+=1
                if arr1[int(i[1:-1])-1][1]>=2:
                    arr1[int(i[1:-1])-1][0]=False
                    left-=1
        elif i[0]=="B" and arr2[int(i[1:-1])-1][0]:
            if i[-1]=="R":
                arr2[int(i[1:-1])-1][0]=False
                right-=1
            elif i[-1]=="Y":
                arr2[int(i[1:-1])-1][1]+=1
                if arr2[int(i[1:-1])-1][1]>=2:
                    arr2[int(i[1:-1])-1][0]=False
                    right-=1
    return (left, right)