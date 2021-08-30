def decode_bits(bin_str):
    return sum(int(j)*(1, -1)[i%2==0] for i,j in enumerate(bin_str))