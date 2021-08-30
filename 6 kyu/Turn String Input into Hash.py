def str_to_hash(st): 
    res={}
    for i in st.split(", "):
        try:
            k, v=i.split("=")
            res[k]=int(v)
        except:
            pass
    return res