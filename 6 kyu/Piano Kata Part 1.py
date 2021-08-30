def black_or_white_key(key_press_count):
    num=(key_press_count-1)%88+1
    if num<=3:
        return "white" if num!=2 else "black"
    return "white" if (num-4)%12 in [0,2,4,5,7,9,11] else "black"
