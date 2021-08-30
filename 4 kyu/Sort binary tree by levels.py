from collections import deque
def tree_by_levels(root):
    if not root:
        return []
    arr=deque([root])
    res=[]
    while arr:
        res.append(arr[-1].value)
        if arr[-1].left:
            arr.appendleft(arr[-1].left)
        if arr[-1].right:
            arr.appendleft(arr[-1].right)
        arr.pop()
    return res