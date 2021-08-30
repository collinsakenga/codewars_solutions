def pin_rook (k, b):
    if (k[1]!=b[1] and k[2]!=b[2]) or (k[1]==b[1] and k[2]==b[2]):
        return []
    elif k[2]==b[2] and b[1] not in "ah":
        if k[1]>b[1]:
            return [f"R{chr(97+i)}{b[2]}" for i in range(ord(b[1])-97)]
        return [f"R{chr(97+i)}{b[2]}" for i in range(ord(b[1])-97+1, 8)]
    elif k[1]==b[1] and b[2] not in "18":
        if k[2]>b[2]:
            return [f"R{b[1]}{chr(49+i)}" for i in range(ord(b[2])-49)]
        return [f"R{b[1]}{chr(49+i)}" for i in range(ord(b[2])-49+1, 8)]
    return []