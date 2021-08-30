def valid_word(seq, word): 
    check=set(seq)
    def helper(count, index):
        if index>=len(word):
            return True if count>=1 else False
        return any(helper(count+1, i) for i in range(index+1, len(word)+1) if word[index:i] in seq)
    return helper(0, 0)