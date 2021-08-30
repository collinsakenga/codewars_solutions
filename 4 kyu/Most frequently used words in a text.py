def top_3_words(text):
    text=text.replace(","," ").replace("."," ").replace(":"," ").replace("!"," ").replace("?"," ").replace("/"," ").replace(";"," ").replace("-"," ").replace("_"," ")
    if text=="  '''  "or text=="  '  ":
        return []
    dict={}
    for i in text.lower().split():
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    list1={k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    result=[]
    for i in list1:
        result.append(i)
        if len(result)==3:
            break
    return result 