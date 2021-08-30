def parse_html_color(color):
    dict={}
    if PRESET_COLORS.get(color.lower(), None):
        temp=PRESET_COLORS[color.lower()][1:]
        rgb=[temp[i:i+2] for i in range(0, len(temp)-1, 2)]
        for i,j in zip("rgb", rgb):
            dict[i]=int(j, 16)
    elif len(color)==4:
        dict={i:int(j+j, 16) for i,j in zip("rgb", color[1:])}
    elif len(color)==7:
        dict={i:int(j, 16) for i,j in zip("rgb", (color[i:i+2] for i in range(1, len(color), 2)))}
    return dict