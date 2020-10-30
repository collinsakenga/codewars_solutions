def compute_sum(n):
    return sum(sum(int(num) for num in str(i)) for i in range(1, n+1))
