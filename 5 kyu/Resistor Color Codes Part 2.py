dict={"k":1000, "m":1000000}
color={0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white'}
def encode_resistor_colors(ohms_string):
    value=ohms_string.split()[0]
    value=str(int(float(value))) if not value[-1].isalpha() else str(int(float(value[:-1])*dict[value[-1].lower()]))
    res=[color[len(value)-2],"gold"]
    for i in range(1,-1,-1):
        res.insert(0,color[int(value[i])])
    return " ".join(res)
        
    