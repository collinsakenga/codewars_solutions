def pyramid(height, material, space=" "):
    return "\n".join(f"{space*(height-1-i)}{material*(i*2+1)}{space*(height-1-i)}" for i in range(height))
