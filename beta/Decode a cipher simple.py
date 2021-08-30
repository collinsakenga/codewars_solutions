from string import ascii_lowercase, ascii_uppercase
def decode(cipher, b, c):
    table={i:j for i,j in enumerate(ascii_lowercase+ascii_uppercase)}
    return "".join(table[i-j-b-c] for i,j in zip(cipher, [0]+cipher))