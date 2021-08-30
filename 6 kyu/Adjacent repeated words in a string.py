def count_adjacent_pairs(st): 
    st=st.lower().split()
    total=0
    i=0
    while True:
        if i>len(st)-2:
            break
        if st[i]==st[i+1]:
            total+=1
            while True:
                i+=1
                if i>len(st)-2 or st[i]!=st[i+1]:
                    break
        i+=1
    return total
                