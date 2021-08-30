from collections import deque
class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    res=deque([tree_root])
    data=[tree_root.data]
    while res:
        temp=res[0]
        res.popleft()
        if not temp.child_nodes:
            continue
        for i in temp.child_nodes:
            res.append(i)
            data.append(i.data)
    return data