word=["Burger","Fries","Chicken","Pizza","Sandwich","Onionrings","Milkshake","Coke"]
def get_order(order):
    res=[]   
    for i in word:
        temp="".join(order.split(i.lower()))
        for _ in range(0,(len(order)-len(temp))//len(i)):
            res.append(i)
    return " ".join(res)
    
        