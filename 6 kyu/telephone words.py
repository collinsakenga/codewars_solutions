from itertools import product
dict={'0': '0', '1': '1', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
def telephone_words(digit_string):
    res=set()
    permute=[list(dict[i]) for i in digit_string]
    for i in product(*permute):
        res.add("".join(i))
    return res