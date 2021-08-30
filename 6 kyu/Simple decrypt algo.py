from collections import defaultdict
def decrypt(test_key):
    table=defaultdict(int)
    for i in test_key:
        table[i]+=1
    return "".join(f"{table[i]}" for i in "abcdefghijklmnopqrstuvwxyz")