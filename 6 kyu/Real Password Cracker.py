from itertools import product
from hashlib import sha1
def password_cracker(hash):
    for i in range(5):
        for j in product("abcdefghijklmnopqrstuvwxyz", repeat=i+1):
            if sha1("".join(j).encode('utf-8')).hexdigest()==hash:
                return "".join(j)
    
    