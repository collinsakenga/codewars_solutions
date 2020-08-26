def solution(array_a, array_b):
    return sum([abs(array_b[i]-array_a[i])**2 for i in range(len(array_a))])/len(array_a) if len(array_a) == len(array_b) else 0
