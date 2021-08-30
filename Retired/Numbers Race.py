def race_numbers(n,m,k):
    count1=count2=0
    n1, m1=n, m
    for i in range(k):
        if n1>m1:
            n1*=2
            m1**=2
            count1+=1
        elif m1>n1:
            n1**=2
            m1*=2
            count2+=1
        else:
            return "Draw"
    return [n, count1-count2] if count1>count2 else [m, count2-count1]
        