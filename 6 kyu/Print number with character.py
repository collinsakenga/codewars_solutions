def print_number(number, char): 
    zero=[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0]]
    one=[[0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1]]
    two=[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
    three=[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0]]
    four=[[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1]]
    five=[[1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 0]]
    six=[[0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0]]
    seven=[[1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0]]
    eight=[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0]]
    nine=[[0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0]]
    res=[char*40, char+" "*38+char]
    number="{:05d}".format(number)
    for i in range(6):
        temp=char+"  "
        temp2=[]
        for num in number:
            str=""
            for j in range(6):
                if num=="0":
                    str+=char if zero[i][j]==1 else " "
                elif num=="1":
                    str+=char if one[i][j]==1 else " "
                elif num=="2":
                    str+=char if two[i][j]==1 else " "
                elif num=="3":
                    str+=char if three[i][j]==1 else " "
                elif num=="4":
                    str+=char if four[i][j]==1 else " "
                elif num=="5":
                    str+=char if five[i][j]==1 else " "
                elif num=="6":
                    str+=char if six[i][j]==1 else " "
                elif num=="7":
                    str+=char if seven[i][j]==1 else " "
                elif num=="8":
                    str+=char if eight[i][j]==1 else " "
                elif num=="9":
                    str+=char if nine[i][j]==1 else " "
            temp2.append(str)
        temp+=" ".join(temp2)+"  "+char
        res.append(temp)
    res.append(char+" "*38+char)
    res.append(char*40)
    print("\n".join(res))
    return "\n".join(res)