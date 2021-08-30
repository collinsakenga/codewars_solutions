def compound_match(words, target):
    dict={}
    for j in set(words):
        if not dict.get(j, None):
            dict[j]="1"
    for i in range(1, len(target)):
        pre=target[:i]
        post=target[i:]
        if dict.get(pre, None) and dict.get(post, None):
            if words.index(pre)>words.index(post):
                return [post,pre,[words.index(pre), words.index(post)]]
            return [pre,post,[words.index(pre), words.index(post)]]