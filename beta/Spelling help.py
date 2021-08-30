def switch(strng, words):
    table={i:j for i,j in words}
    return (" " if strng and strng[0]==" " else "")+" ".join(table.get(i, i) for i in strng.split())