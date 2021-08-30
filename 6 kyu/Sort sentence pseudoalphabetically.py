def pseudo_sort(st): 
    st=st.replace(",","").replace(".","").replace("?","").replace("!","").replace(",","").replace(":","").replace(";","")
    st=st.split()
    resultCap=[]
    resultLow=[]
    for word in st:
        if word[0].isupper():
            resultCap.append(word)
        else:
            resultLow.append(word)
    resultCap.sort(reverse=True)
    resultLow.sort()
    if not resultLow:
        return " ".join(resultCap)
    elif not resultCap:
        return " ".join(resultLow)
    return " ".join(resultLow)+" "+" ".join(resultCap)