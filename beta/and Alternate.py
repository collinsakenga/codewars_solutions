def encode_string(string):
    return "".join(["....", "!!"][i%2] for i in range(len(string)))