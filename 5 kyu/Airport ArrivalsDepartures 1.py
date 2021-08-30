def flap_display(lines, rotors):
    for i in range(len(lines)):
        lines[i]=list(lines[i])
    for _ in range(len(rotors)):
        for i in range(len(rotors[_])):
            for k in range(i, len(lines[_])):
                lines[_][k]=ALPHABET[(ALPHABET.index(lines[_][k])+rotors[_][i])%len(ALPHABET)]
    for i in range(len(lines)):
        lines[i]="".join(lines[i])
    return lines