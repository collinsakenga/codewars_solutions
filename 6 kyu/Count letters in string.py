from collections import Counter
def letter_count(s):
    return Counter("".join(sorted(s)))