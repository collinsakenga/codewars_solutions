def match_words(acronym,words):
    dict={k:"" for k in acronym}
    for i in words:
        dict[next(j for j in i if j in dict)]=i
    return dict