class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def is_bst(node):
    if not node:
        return True
    flag=None
    if node.left:
        if node.left.value==node.value:
            return False
        flag=True if node.left.value<node.value else False
    if node.right:
        if node.right.value==node.value:
            return False
        if flag==None:
            flag=True if node.right.value>node.value else False
        else:
            if (flag==True and node.right.value<node.value) or (flag==False and node.right.value>node.value):
                return False
    if flag==None: 
        return True 
    return helper(node, flag)
def helper(node, flag, direction=[]):
    if node==None:
        return True
    if node.left:  
        if node.left.value==node.value:
            return False
        if (flag and node.left.value>node.value):
            return False
        if (flag==False and node.left.value<node.value):
            return False
        for i,j in direction:
            if j==False:
                if (flag and node.left.value<i) or (not flag and node.left.value>i):
                    return False
            else:
                if (flag and node.left.value>i) or (not flag and node.left.value<i):
                    return False
    if node.right: 
        if node.right.value==node.value:
            return False
        if (flag and node.right.value<node.value):
            return False
        if (flag==False and node.right.value>node.value):
            return False
        for i,j in direction:
            if j==False:
                if (flag and node.right.value<i) or (not flag and node.right.value>i):
                    return False
            else:
                if (flag and node.right.value>i) or (not flag and node.right.value<i): 
                    return False
    return helper(node.left, flag, direction+[[node.value, True]]) and helper(node.right, flag, direction+[[node.value, False]])