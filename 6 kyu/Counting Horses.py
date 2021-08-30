def count_horses(sound_str):
    res=[]
    while True:
        string=list(sound_str)
        temp=len(res)
        for i,j in enumerate(sound_str):
            if j!="0":
                res.append(i+1)
                for k in range(i, len(string), i+1):
                    string[k]=str(int(string[k])-1)
                break
        if temp==len(res):
            return res
        sound_str="".join(string)