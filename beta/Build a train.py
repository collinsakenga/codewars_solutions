def train(s):
    return sum({"A":15, "B":10, "C":7, "D":8}.get(i, 5) for i in s)