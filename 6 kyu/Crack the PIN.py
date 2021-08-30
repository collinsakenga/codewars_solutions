import hashlib
def crack(hash):
    for i in range(0,100000):
        if hashlib.md5("{0:05d}".format(i).encode('utf-8')).hexdigest()==hash:
            return "{0:05d}".format(i)