from collections import deque
def do_breadth_first_traversal(binary_tree):
    res=deque([binary_tree])
    tags=[]
    while res:
        data=res.popleft()
        if data:
            tags.append(data.tag)
        if data and data.left:
            res.append(data.left)
        if data and data.right:
            res.append(data.right)
    return tags