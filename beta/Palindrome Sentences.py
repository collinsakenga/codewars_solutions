def is_palindrome_sentence(s):
    res="".join(i.lower() for i in s if i.isalnum())
    return res==res[::-1]