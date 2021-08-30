import numpy
def solve_eq(eq):
    a=[]
    b=[]
    for i in eq:
        a.append(i[:-1])
        b.append(i[-1])
    equations=numpy.array(a)
    ans=numpy.array(b)
    return [round(i) for i in numpy.linalg.solve(equations, ans)]
   