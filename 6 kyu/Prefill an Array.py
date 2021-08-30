def prefill(n,v=None):
    if type(n)!=int:
        try:
            n=int(n)
        except:
            raise TypeError(n+" is invalid") if n else TypeError("None is invalid")
    return [v]*n if v else [None]*n