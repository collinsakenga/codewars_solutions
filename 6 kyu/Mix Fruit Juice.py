dict={'banana': 5, 'orange': 5, 'apple': 5, 'lemon': 5, 'grapes': 5, 'avocado': 7, 'strawberry': 7, 'mango': 7}
def mix_fruit(arr):
    return round(sum(9 if not dict.get(i.lower(), None) else dict[i.lower()] for i in arr)/len(arr))