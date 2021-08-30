from collections import defaultdict
def total_item(lst):
    result = defaultdict(int)
    for i in lst:
        if isinstance(i, bool):
            result["Boolean"]+=1
        elif isinstance(i, int):
            result["Integer"]+=1
        elif isinstance(i, dict):
            result["Dictionary"]+=1
        elif isinstance(i, list):
            result["List"]+=1
        elif isinstance(i, tuple):
            result["Tupple"]+=1
        elif isinstance(i, str):
            result["String"]+=1
        elif isinstance(i, float):
            result["Float"]+=1
    return result