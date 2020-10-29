def inside_out(st):
    res=[]
    for i in st.split():
        if len(i)%2==0:
            res.append(i[:len(i)//2][::-1]+i[len(i)//2:][::-1])
        else:
            res.append(i[:len(i)//2][::-1]+i[len(i)//2]+i[len(i)//2+1:][::-1])
    return " ".join(res)