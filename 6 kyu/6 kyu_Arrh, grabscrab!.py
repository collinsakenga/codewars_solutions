from collections import Counter


def grabscrab(word, possible_words):
    return [i for i in possible_words if Counter(i) == Counter(word)]
