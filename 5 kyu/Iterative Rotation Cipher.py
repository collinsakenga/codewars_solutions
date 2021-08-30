import numpy as np

def encode(n, strng):
    strcopy = strng
    count = 0
    while count < n:
        list1 = list(strcopy.split(' '))
        first = ''.join(np.roll(np.array(list(''.join(list1))), n))
        list2 = []
        start = 0
        for i in list1:
            if i == '':
                list2.append('')
            else:
                length = len(i)
                slice = first[start:start + length]
                list2.append(slice)
                start += length
        list3 = []
        for i in list2:
            if i == '':
                list3.append('')
            else:
                list3.append(''.join(np.roll(np.array(list(i)), n)))
        strcopy = ' '.join(list3)
        count += 1
    return str(n) + ' ' + strcopy

def decode(strng):
    n = int(strng.split()[0])
    encoded = strng.split(' ')[1:]
    count = 0
    strcopy = encoded

    while count < n:
        list1 = []
        for i in strcopy:
            list1.append(''.join(np.roll(np.array(list(i)), -n)))
        first = ''.join(np.roll(np.array(list(''.join(list1))), -n))
        list2 = []
        start = 0
        for i in encoded:
            if i == ' ':
                list2.append(' ')
            else:
                length = len(i)
                slice = first[start:start + length]
                list2.append(slice)
                start += length
        strcopy = list2
        count += 1
    return ' '.join(strcopy)