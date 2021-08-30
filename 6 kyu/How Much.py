def howmuch(m, n):
    return [[f"M: {i}",f"B: {5+i//63*9}" ,f"C: {4+i//63*7}" ] for i in range(min(m,n), max(m, n)+1) if ( i>=37 and (i-37)%63==0)]