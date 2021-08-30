from collections import Counter
def slot_machine(results):
    return sum(4 if len(set(i))==2 and i.count(i[0])==3 else [0, 2, 10, 100, 1000][max(0, Counter(i).most_common()[0][1]-2)] for i in results)-len(results)