def max_profit(prices):
    minimum=float("inf")
    maximum=-1
    for i in prices:
        if i<minimum:
            minimum=i
        elif (i-minimum)>maximum:
            print(i-minimum)
            maximum=i-minimum
    return maximum