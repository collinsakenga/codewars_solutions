from itertools import groupby
def sort_strings_by_vowels(seq): 
    def helper(x):
        for i in "aeiou":
            x=x.replace(i, "a")
        return max((len(tuple(j)) for i,j in groupby(x) if i=="a"), default=0)
    return sorted(seq, key=lambda x: -helper(x.lower()))