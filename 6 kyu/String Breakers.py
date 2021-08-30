def string_breakers(n, st): 
    s="".join(i for i in st if i!=" ")
    return "\n".join(s[i:i+n] for i in range(0, len(s), n))