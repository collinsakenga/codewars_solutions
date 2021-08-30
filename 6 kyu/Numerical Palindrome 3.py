def palindrome(num):
    if not isinstance(num, int) or num<0:
        return 'Not valid'
    check=str(num)
    total=0
    for i in range(2, len(check)+1):
        for j in range(len(check)-i+1):
            if is_palin(check[j:j+i]):
                total+=1
    return total
def is_palin(s):
    return s[::-1]==s