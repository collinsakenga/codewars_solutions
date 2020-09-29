def whitespace_number(n):
    return ("\t" if n < 0 else " ")+"".join("\t" if i == "1" else " " for i in bin(abs(n))[2:].lstrip("0"))+"\n"
