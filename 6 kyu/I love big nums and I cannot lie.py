from itertools import cycle
def biggest(numbers):
    length=max(len(str(i)) for i in numbers)+1
    res=sorted(numbers, key=lambda x: (-helper(x, length))) 
    return str(int("".join(str(i) for i in res)))
def helper(s, length):
    iter=cycle(str(s))
    return int("".join(next(iter) for i in range(length))) 
 