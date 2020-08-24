def find_nb(cubenum):
    total=1
    index=2
    comp=-1
    while True:
        total+=index**3
        if total==cubenum:
            comp=index
            break
        if total>cubenum:
            break
        index+=1
    return(comp)