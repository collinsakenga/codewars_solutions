# return the two oldest ages in the array of ages passed in.
# it should return the two ages as a sorted array, youngest age first
def red_knight(N, P):
    return ('Black' if (N+P)%2 else "White", P*2)