def ka_co_ka_de_ka_me(word):
    res=""
    temp=""
    for j in word:
        if j in "aeiouAEIOU":
            temp+=j
        else:
            res+=temp+"ka"+j if temp else j
            temp=""
    return "ka"+res+temp