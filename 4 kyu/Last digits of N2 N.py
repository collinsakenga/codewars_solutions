GREEN = [0, 1]
p, f, s = 1, 5, 6
def green(n):
    global p, f, s
    while n >= len(GREEN):
        q = 10 * p
        # f, s = f**2 % q, (1 - (s-1)**2) % q
        f, s = pow(f, 2, q), 2*s - pow(s, 2, q)
        if s < 0: s += q
        GREEN.extend(sorted(n for n in (f, s) if n > p))
        p = q
    return GREEN[n]