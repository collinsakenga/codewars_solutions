def anagrams(word, words):
    flag = True
    result = []
    index = 0
    wordSet = set(words[index])
    while True:
        for char in wordSet:
            if words[index].count(char) != word.count(char):
                flag = False
                break
        if flag:
            result.append(words[index])
        index += 1
        if index == len(words):
            break
        flag = True
        wordSet = set(words[index])
    return result
