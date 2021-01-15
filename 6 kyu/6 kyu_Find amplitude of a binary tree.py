def tree_amplitude(root_node):
    temp=helper(root_node, [], []) or [0]
    return max(temp)
def helper(root_node, arr, res):
    if root_node==None:
        if arr:
            compare=list(i.data for i in arr)
            res.append(max(compare)-min(compare))
        return 
    helper(root_node.left, arr+[root_node], res)
    helper(root_node.right, arr+[root_node], res)
    return res