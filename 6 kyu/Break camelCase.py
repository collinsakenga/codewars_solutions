def solution(s):
    return "".join(char.replace(char," "+char) if char.isupper() else char for char in s)