from itertools import permutations


def get_words(hash_of_letters):
    check = ""
    total = 0
    res = set()
    for i, j in hash_of_letters.items():
        check += "".join(j)*i
        total += i*len(j)
    for i in permutations(check, total):
        res.add("".join(i))
    return sorted(res)
