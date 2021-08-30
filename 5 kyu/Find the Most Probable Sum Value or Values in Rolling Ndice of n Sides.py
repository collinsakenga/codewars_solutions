from math import factorial
from itertools import product
dict={'tetrahedral': [1, 4], 'cubic': [1, 6], 'octahedral': [1, 8], 'ninesides': [1, 9], 'tensides': [1, 10], 'dodecahedral': [1, 12], 'icosahedral': [1, 20]}
def most_prob_sum(dice, n):
    num=sum(dict[dice])*n
    total=dict[dice][1]**n
    if num%2==1:
        count=sum(((num//2)<=sum(i)<=(num//2+1) for i in product([j+1 for j in range(dict[dice][1])], repeat=n)))/2
        return [[num//2, num//2+1], count/total]
    count=sum((num//2==sum(i) for i in product([j+1 for j in range(dict[dice][1])], repeat=n)))
    return [[num//2], count/total]
def combination(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))