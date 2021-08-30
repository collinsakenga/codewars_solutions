dict={"antelope": ["grass"],"big-fish": ["little-fish"],"bug": ["leaves"],"bear": ["big-fish","chicken","bug","cow","leaves","sheep"],"chicken": ["bug"],
      "cow": ["grass"],"fox": ["chicken", "sheep"],"giraffe": ["leaves"],"lion": ["antelope", "cow"],"panda": ["leaves"],"sheep": ["grass"]}
def who_eats_who(zoo):
    res=[zoo]
    rec=zoo.split(",")
    temp=[]
    while len(rec)>1:
        flag=False
        for i in range(len(rec)):
            if rec[i] not in dict:
                continue
            if (i-1)>=0 and rec[i-1] in dict[rec[i]]:
                temp.append(f"{rec[i]} eats {rec[i-1]}")
                flag=True
                rec.pop(i-1)
                break
            if (i+1)<len(rec) and rec[i+1] in dict[rec[i]]:
                temp.append(f"{rec[i]} eats {rec[i+1]}")
                flag=True
                rec.pop(i+1)
                break
        if not flag:
            break
    for i in temp:
        res.append(i)
    return res+[",".join(rec)]