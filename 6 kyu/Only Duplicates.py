from collections import Counter
def only_duplicates(string):
    check=Counter(string)
    return "".join(i for i in string if check[i]>1)