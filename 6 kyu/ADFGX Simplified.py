dict={i:j for i,j in enumerate(['A', 'D', 'F', 'G', 'X'])}
dict2={j:i for i,j in dict.items()}
def adfgx_encrypt(plaintext, square):
    plaintext=plaintext.replace("j", "i") if "i" in square else plaintext.replace("i", "j")
    matrix={j:(i//5, i%5) for i,j in enumerate(square)}
    return "".join(dict[matrix[i][0]]+dict[matrix[i][1]] for i in plaintext)
def adfgx_decrypt(ciphertext, square):
    matrix=[list(square[i*5:i*5+5]) for i in range(5)]
    return "".join(matrix[dict2[ciphertext[i]]][dict2[ciphertext[i+1]]] for i in range(0, len(ciphertext), 2))