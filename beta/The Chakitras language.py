def chakitra_language(sentence):
    return all(ord(max(j for j in i))%2==0 for i in sentence.split())