dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2,
        'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}


def get_best_word(points, words):
    return words.index(sorted(words, key=lambda x: (-score(x), len(x), words.index(x)))[0])


def score(s):
    total = 0
    for i in s:
        total += dict[i]
    return total
