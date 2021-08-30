def decrypt(code):
    return "".join(" abcdefghijklmnopqrstuvwxyz"[sum(int(j) for j in i if j.isdigit())%27] for i in code.split())