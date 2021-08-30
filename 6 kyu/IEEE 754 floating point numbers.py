import struct
def float_to_IEEE_754 (f : float) -> str :
    res=float_to_bin(f)
    return res[0]+" "+res[1:12]+" "+res[12:]

# https://stackoverflow.com/questions/8751653/how-to-convert-a-binary-string-into-a-float-value/8762541#8762541
def float_to_bin(value):  
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return '{:064b}'.format(d)
