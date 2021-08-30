def rotate_in_place(matrix):
    temp=[[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            matrix[i][j]=temp[i][j]
    return matrix