def sum_diff(a, b, c):
    return b-(1, -1)[a%2==1]*c if b>c else c-(1, -1)[a%2==1]*b