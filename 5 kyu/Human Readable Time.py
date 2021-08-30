def make_readable(seconds):
    hr = seconds//3600
    min = seconds//60 % 60
    sec = seconds % 60
    return f"{add_zero(hr)}:{add_zero(min)}:{add_zero(sec)}"
def add_zero(n):  
    return f"0{n}" if (n >= 0 and n <= 9) else f"{n}"