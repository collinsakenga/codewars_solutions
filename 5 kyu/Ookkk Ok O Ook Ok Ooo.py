def okkOokOo(s):
    res=s[:-1].split("?")
    string=""
    for i in range(len(res)):
        res[i]="".join(res[i].split(", ")).strip().lower()
        res[i]=res[i].replace("o","0").replace("k","1")      
        string+=chr(int(res[i], 2))
    return string