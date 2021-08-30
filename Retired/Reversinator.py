def reversinator(s):
    return int(bin(int("".join(f"{ord(i)-96}" for i in s[::-1])))[2:])