def matrixfy(st):
    if not st:
        return "name must be at least one letter"
    res=st if len(st)**0.5==int(len(st)**0.5) else st.ljust((int(len(st)**0.5)+1)**2, ".")
    return [list(res[i:i+int(len(res)**0.5)]) for i in range(0, len(res), int(len(res)**0.5))]