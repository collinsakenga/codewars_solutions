def strip_it(code):
    temp = code.split("\n")
    for i, j in enumerate(temp):
        paragraph = j
        while True:
            if paragraph.count("/*") == 0 and paragraph.count("*/") == 0 and paragraph.count("//") == 0:
                break
            if paragraph.count("//"):
                paragraph = paragraph[:paragraph.index("//")]
            elif paragraph.count("/*") and paragraph.count("*/"):
                index = paragraph.index("/*")
                index2 = paragraph[paragraph.index("/*"):].index("*/")
                paragraph = paragraph[:index]+paragraph[index+index2+2:]
        temp[i] = paragraph
    return "\n".join(temp)
