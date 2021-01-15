def build_table(text, style):
    if not text:
        return ""
    lengths=[-float("inf") for i in range(len(text[0]))]
    for i in text:
        for j,k in enumerate(i):
            lengths[j]=max(lengths[j], len(k)+style.off_min*2)
    res=[style.sep_he*(sum(lengths)+len(style.sep_vi)*(len(lengths)-1)+len(style.sep_ve)*2)]
    key=str.maketrans(" ", style.sep_hi)
    for i in text:
        temp=[]
        for j,k in enumerate(i):
            if style.align=="left":
                temp.append(style.off_min*style.sep_hi+k+(lengths[j]-len(k)-style.off_min)*style.sep_hi) 
            elif style.align=="mid":
                left=right=(lengths[j]-len(k))//2
                if (lengths[j]-len(k))%2:
                    right+=1
                temp.append(style.sep_hi*left+k+style.sep_hi*right)
            elif style.align=="right":
                temp.append((lengths[j]-len(k)-style.off_min)*style.sep_hi+k+style.off_min*style.sep_hi)
        res.append(style.sep_ve+style.sep_vi.join(temp).translate(key)+style.sep_ve)
    return "\n".join(res)