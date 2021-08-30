from functools import lru_cache
def calc(cards):
    return helper(tuple(cards),1)
@lru_cache(maxsize=None)
def helper(cards, power):
    if len(cards)==1:
        return 2**power*cards[0]
    return max(cards[0]*(2**power)+helper(cards[1:], power+1), cards[-1]*(2**power)+helper(cards[:-1], power+1))