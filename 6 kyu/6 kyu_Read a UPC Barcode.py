def read_barcode(barcode):
    dict = {"▍": "1", " ": "0"}
    res = barcode.translate(barcode.maketrans(dict))
    decoded = []
    for i in range(3, 7*6+3, 7):
        decoded.append(LEFT_HAND[res[i:i+7]])
    for i in range(7*6+3+5, len(res)-3, 7):
        decoded.append(RIGHT_HAND[res[i:i+7]])
    second = "".join(str(i) for i in decoded[1:6])
    third = "".join(str(i) for i in decoded[6:11])
    return f"{decoded[0]} {second} {third} {decoded[-1]}"
