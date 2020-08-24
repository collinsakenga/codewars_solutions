def ip_to_int32(ip):
    temp = ""
    ip = ip.split(".")
    for i in ip:
        temp += "{0:08b}".format(int(i))
    return int(temp, 2)
