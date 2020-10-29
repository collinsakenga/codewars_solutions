from collections import Counter
def is_isogram(word):
    if not isinstance(word, str) or not word:
        return False
    check=Counter(i.lower() for i in word if i.isalpha())
    return False if not check else True if check.most_common()[0][1]==check.most_common()[-1][1] else False