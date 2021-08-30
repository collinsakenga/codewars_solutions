from collections import deque
def readable_size(b):
    bytes=iter(["B", "KB", "MB", "GB", "TB", "PB"])
    res=deque([])
    while b>0:
        num, byte=b%1024, next(bytes)
        if num>0:
            res.appendleft(f"{num} {byte}")
        b//=1024
    if len(res)<=2:
        return ", ".join(res)
    last=res.pop()
    return ", ".join(res)+f" and {last}"