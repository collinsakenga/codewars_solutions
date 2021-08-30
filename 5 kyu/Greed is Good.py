def score(dice):
    total=0
    comp=0
    while True:
        if dice.count(1)>=3:
            total+=1000
            for i in range(3):
                dice.remove(1)
        elif dice.count(6)>=3:
            total+=600
            for i in range(3):
                dice.remove(6)
        elif dice.count(5)>=3:
            total+=500
            for i in range(3):
                dice.remove(5)
        elif dice.count(4)>=3:
            total+=400
            for i in range(3):
                dice.remove(4)
        elif dice.count(3)>=3:
            total+=300
            for i in range(3):
                dice.remove(3)
        elif dice.count(2)>=3:
            total+=200
            for i in range(3):
                dice.remove(2)
        elif dice.count(1)>=1 and dice.count(1)<3:
            total+=100
            dice.remove(1)
        elif dice.count(5)>=1 and dice.count(5)<3:
            total+=50
            dice.remove(5)
        if total>comp:
            comp=total
        elif total==comp:
            break
    return comp       