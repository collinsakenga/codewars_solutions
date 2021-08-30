def calculate_string(st): 
    return str(int(round(eval("".join(i for i in st if i.isdigit() or i in "+-./*")))))