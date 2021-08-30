def order(sentence):
    sentence=sentence.split()
    result=[]
    for num in range(1,len(sentence)+1):
        for word in sentence:
            if str(num) in word:
                result.append(word)
                break
    return " ".join(result)