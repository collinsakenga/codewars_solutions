from random import randint
letters="abcdefghijklmnopqrstuvwxyz"
def generateName():
    while True:
        res="".join(letters[randint(0, 25)] for i in range(6))
        if not photoManager.nameExists(res):
            return res