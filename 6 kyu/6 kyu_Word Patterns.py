def word_pattern(pattern, string):
    string = string.split()
    if len(pattern) != len(string) or len(set(pattern)) != len(set(string)):
        return False
    dict = {}
    for i in range(len(pattern)):
        if not dict.get(pattern[i], None):
            dict[pattern[i]] = string[i]
        if dict[pattern[i]] != string[i]:
            return False
    return True
