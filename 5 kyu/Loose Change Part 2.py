def loose_change(coins_list, amount_of_change):
    coins_list=sorted(coins_list, reverse=True)
    compare=float("inf")
    for i in range(len(coins_list)):
        compare=min(compare, helper(coins_list[i:], amount_of_change))
    return compare
def helper(arr, num):
    total=0
    for i in arr:
        total+=num//i
        num-=num//i*i
    return total