def reversi_row(moves):
    res=["."]*8
    for i,j in enumerate(moves):
        res[j]="*" if i%2==0 else "O"
        first={k:-1 for k,l in enumerate(res) if l==["*", "O"][i%2==1]}
        second=[k for k,l in enumerate(res) if l==["*", "O"][i%2==0]]
        temp=[]
        third=[]
        for k in second:
            if not temp:
                temp=[k]
            elif k-temp[-1]==1:
                temp.append(k)
            else:
                third.append(temp)
                temp=[k]
        third=third+[temp] if temp else third
        for k in third:
            if (j==min(k)-1 or j==max(k)+1) and first.get(min(k)-1, None) and first.get(max(k)+1, None):             
                for l in range(min(k), max(k)+1):
                    res[l]="*" if i%2==0 else "O"
    return "".join(res)