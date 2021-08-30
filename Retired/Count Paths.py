from functools import lru_cache
def count_paths(w, h):
    return helper(1, 1, w, h)
@lru_cache(maxsize=None)
def helper(curx, cury, limitx, limity):
    if curx==limitx and cury==limity:
        return 1
    elif curx==limitx:
        return helper(curx, cury+1, limitx, limity)
    elif cury==limity:
        return helper(curx+1, cury, limitx, limity)
    return helper(curx, cury+1, limitx, limity)+helper(curx+1, cury, limitx, limity)