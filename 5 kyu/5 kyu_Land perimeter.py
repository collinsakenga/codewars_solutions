def land_perimeter(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "O":
                continue
            count = 4
            if (i-1) >= 0:
                if arr[i-1][j] == "X":
                    count -= 1
            if (j-1) >= 0:
                if arr[i][j-1] == "X":
                    count -= 1
            if (i+1) < len(arr):
                if arr[i+1][j] == "X":
                    count -= 1
            if (j+1) < len(arr[i]):
                if arr[i][j+1] == "X":
                    count -= 1
            total += count
    return f"Total land perimeter: {total}"
