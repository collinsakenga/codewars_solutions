def numberOfSteps(steps, m):
    if m>steps:
        return -1
    print(steps, m)
    return m*(steps//2//m+1) if steps/2%m else m*(steps//2//m)