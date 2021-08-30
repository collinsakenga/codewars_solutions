from collections import deque
def battle_codes(arr, num):
    if not arr or not num:
        return "Peace"
    arr1, arr2=deque(list(arr)), deque(list(num))
    while arr1 and arr2:
        letter=ord(arr2[0])
        for i in range(min(len(arr2), 1)):
            arr2[i]=chr(ord(arr2[i])-(ord(arr1[-1])-ord("a")+1))
        for i in range(len(arr1)-1, max(-1, len(arr1)-3), -1):
            arr1[i]=chr(ord(arr1[i])-(letter-ord("0")))
        if arr2[0] not in "123456789":
            arr2.popleft()
        if len(arr1)>=2 and arr1[-2] not in "abcdefghijklmnopqrstuvwxyz":
            temp=arr1.pop()
            arr1.pop()
            arr1.append(temp)
        if len(arr1)>=1 and arr1[-1] not in "abcdefghijklmnopqrstuvwxyz":
            arr1.pop()
    if not arr1 and not arr2:
        return "Draw"
    elif not arr1:
        return "".join(arr2)
    elif not arr2:
        return "".join(arr1)  