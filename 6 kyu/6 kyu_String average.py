dict = {"zero": 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
dict2 = {0: "zero", 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}


def average_string(s):
    if not s:
        return "n/a"
    total = 0
    for i in s.split():
        try:
            total += dict[i]
        except:
            return "n/a"
    return dict2[total//len(s.split())]
