from collections import Counter


def longest_palindrome(s):
    s = s.lower()
    check = Counter(s)
    even = 0
    odd = 0
    for i in check:
        if check[i] % 2 == 0 and i.isalnum():
            even += check[i]
        elif check[i] % 2 == 1 and i.isalnum():
            odd = max(odd, check[i])
            even += check[i]-1
    return even+1 if odd else even
