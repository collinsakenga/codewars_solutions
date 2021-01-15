from itertools import cycle
def penalty(a_list):
    longest=max(len(i) for i in a_list)
    res=sorted(a_list, key=lambda x: helper(x, longest+1))
    return "".join(res)
def helper(s, longest):
    iter=cycle(s)
    return int("".join(next(iter) for i in range(longest))) 