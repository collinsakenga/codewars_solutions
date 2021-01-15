def testit(s):
    return "".join(chr((ord(s[i])+ord(s[i+1]))//2) if (i+1)<len(s) else s[i] for i in range(0, len(s), 2))