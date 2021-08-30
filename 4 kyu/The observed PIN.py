from itertools import product
dict={'1': '124', '2': '1235', '3': '236', '4': '1457', '5': '24568', '6': '3569', '7': '478', '8': '57890', '9': '689', '0': '80'}
def get_pins(observed):
    return ["".join(i) for i in product(*(list(dict[j]) for j in observed))]