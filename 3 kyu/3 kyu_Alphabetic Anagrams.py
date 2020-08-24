from math import factorial


def listPosition(word):
    if len(word) == 1:
        return 1
    check = "".join(sorted(word, key=lambda x: x[0]))
    sum = 0
    for i in range(len(check)):
        temp = check.replace("_", "")
        index = check.index(word[i])
        check = check[:index]+"_"+check[index+1:]
        sum += (temp.index(word[i])*combos(temp))//len(temp)
    return sum+1


def combos(word):
    combo = factorial(len(word))
    for i in set(word):
        combo = combo//factorial(word.count(i))
    return combo
