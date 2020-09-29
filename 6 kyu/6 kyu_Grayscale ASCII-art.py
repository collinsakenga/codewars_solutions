from copy import deepcopy
GLYPHS = " .,:;xyYX"


def image2ascii(image):
    res = deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            res[i][j] = GLYPHS[int((image[i][j]*8)/255)]
    return "\n".join("".join(i) for i in res)
