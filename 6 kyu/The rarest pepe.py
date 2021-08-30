from collections import Counter
def find_rarest_pepe(pepes):
    total=Counter(pepes)
    least=total.most_common()[-1]
    if least[1]>=5:
        return 'No rare pepes!'
    res=sorted(k for k,v in total.items() if v==least[1])
    return "".join(res) if len(res)==1 else res
    