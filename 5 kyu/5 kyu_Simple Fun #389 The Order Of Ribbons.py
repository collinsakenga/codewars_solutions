from collections import Counter
def the_order_of(ribbons):
    arr=[list(i) for i in ribbons.split("\n")]
    vertical=horizontal=False
    res=""
    count=1
    while True:
        flag=False
        num=11-(count//2)
        for i in range(len(arr)):
            temp1=""
            temp2=""
            for j in range(len(arr[i])):
                temp1+=arr[i][j]
                temp2+=arr[j][i]
            check1=Counter(k for k in temp1 if k.isdigit()).most_common(1)
            check2=Counter(k for k in temp2 if k.isdigit()).most_common(1)
            if (vertical==horizontal or horizontal) and check1 and check1[0][1]==num:
                flag=True
                vertical=True
                horizontal=False
                res+=next(k for k in temp1 if k==check1[0][0])
                for j in range(len(arr[i])):
                    arr[i][j]="."
            elif (vertical==horizontal or vertical) and check2 and check2[0][1]==num:
                flag=True
                vertical=False
                horizontal=True
                res+=next(k for k in temp2 if k==check2[0][0])
                for j in range(len(arr[i])):
                    arr[j][i]="."
            if flag:
                break
        count+=1
        if not flag:
            break
    return res[::-1]