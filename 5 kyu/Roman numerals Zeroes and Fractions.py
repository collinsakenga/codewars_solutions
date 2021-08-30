roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
dict={1: '.', 2: ':', 3: ':.', 4: '::', 5: ':.:', 6: 'S', 7: 'S.', 8: 'S:', 9: 'S:.', 10: 'S::', 11: 'S:.:'}
def helper(n):
    if n==0:
        return ""
    temp=next(i for i in roman_numerals.keys() if n//i)
    return n//temp*roman_numerals[temp]+helper(n-n//temp*temp)
def roman_fractions(integer, fraction=None):
    if not (0<=integer<=5000) or (fraction and (fraction<0 or fraction>=12)):
        return "NaR" 
    elif integer==0 and not fraction:
        return "N"
    return helper(integer) if not fraction else helper(integer)+dict[fraction]
