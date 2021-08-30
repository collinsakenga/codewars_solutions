def delete_nth(order,max_e):
    order.reverse()
    for int in set(order):
        if order.count(int)>max_e:
            for count in range(order.count(int)-max_e):
                order.remove(int)
    order.reverse()
    return order