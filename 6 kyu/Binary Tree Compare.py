def compare(a, b):
    if a==None and b==None:
        return True
    elif a==None:
        return False
    elif b==None:
        return False
    if a.val==b.val and compare(a.left, b.left) and compare(a.right, b.right):
        return True
    return False
