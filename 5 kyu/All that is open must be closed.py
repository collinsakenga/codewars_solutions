from collections import deque
def is_balanced(source, caps):
    open=[caps[i] for i in range(0, len(caps), 2)]
    close=[caps[i] for i in range(1, len(caps), 2)]
    if open==close:
        for i in open:
            if source.count(i)%2!=0:
                return False
        return True
    pairs=[caps[i:i+2] for i in range(0, len(caps), 2)]
    res=deque()
    for i in source:
        if i in open:
            res.appendleft(i)
        elif i in close:
            if not res or res[0]+i not in pairs:
                return False
            res.popleft()
    return False if res else True