def rank(st, we, n):
    name=st.split(",")
    if not st:
        return "No participants"
    elif len(name)<n:
        return "Not enough participants"
    dict={}
    for i in range(len(name)):
        dict[name[i]]=we[i]*winning_number(name[i])
    dict=sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    return dict[n-1][0]
def winning_number(word):
    word=word.lower()
    total=0
    for i in word:
        total+=ord(i)-ord("a")+1
    return total+len(word)