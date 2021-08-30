def strange_math(n, k):
    return sorted((i+1 for i in range(n)), key=lambda x: str(x)).index(k)+1