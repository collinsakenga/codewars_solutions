dict1={j:i for i,j in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}
dict2={j:i for i,j in dict1.items()}
def caesar_crypto_encode(text, shift):
    if not text or text.count(" ")==len(text):
        return ""
    return "".join(dict2[(dict1[i]+shift)%52] if i.isalpha() else i for i in text)