def trace(matrix):
    try:
        return sum(matrix[i][i] for i in range(max(len(matrix), len(matrix[0]))))
    except:
        return None