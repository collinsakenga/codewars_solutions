def cue(bars,instruments):
    return {j:next((k for k,l in enumerate(i) if l!=" "), len(i)) for i,j in zip(bars.split("\n"), instruments)}
