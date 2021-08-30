def int32_to_ip(int32):
    temp="{0:032b}".format(int32)
    return f"{int(temp[0:8],2)}.{int(temp[8:16],2)}.{int(temp[16:24],2)}.{int(temp[24:32],2)}"
    