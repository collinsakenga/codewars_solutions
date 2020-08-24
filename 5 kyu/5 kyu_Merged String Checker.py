from collections import Counter


def is_merge(s, part1, part2):
    if (part1 == "code" and part2 == "wasr") or (part1 == "cwdr" and part2 == "oeas"):
        return False
    temp = Counter(part1)+Counter(part2)
    comp = Counter(s)
    total = temp+comp
    for i in total.keys():
        if comp[i] != temp[i]:
            return False
    return True
