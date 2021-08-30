base64="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def base64_to_base10(str):
    total=0
    for i,j in enumerate(str):
        total+=base64.index(j)*(64**(len(str)-1-i))
    return total