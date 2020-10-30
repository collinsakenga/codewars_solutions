descend={j:i for i,j in enumerate([ ':D', ':)', ':|', ':(', 'T_T' ])}
ascend={j:i for i,j in enumerate([ ':D', ':)', ':|', ':(', 'T_T' ][::-1])}
def sort_emotions(arr, order):
    return sorted(arr, key=lambda x: descend[x]) if order else sorted(arr, key=lambda x: ascend[x])