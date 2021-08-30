def elemental_forms(word):
    final=helper(word, [], set())
    return [list(i) for i in final]
def helper(word, cur, res):
    if not word:
        res.add(tuple(cur))
        return
    for i in range(3):
        prefix=word[:i+1].capitalize()
        if prefix in ELEMENTS:
            helper(word[i+1:], cur+[f"{ELEMENTS[prefix]} ({prefix})"], res)
    return res