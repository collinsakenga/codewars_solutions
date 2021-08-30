from collections import Counter
def letter_frequency(text):  
    return sorted(Counter("".join(i for i in text.lower() if i.isalpha())).items(), key=lambda x: (-x[1], ord(x[0])))