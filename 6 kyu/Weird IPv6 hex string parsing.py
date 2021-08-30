def parse_IPv6(iPv6):
    res=""
    for i in range(0, len(iPv6), 5):
        res+=str(hex_sum(iPv6[i:i+4]))
    return res
def hex_sum(s):
    return sum(int(i, 16) for i in s)