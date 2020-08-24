def pick_peaks(arr):
    pos = []
    peaks = []
    index = 1
    while index < len(arr)-1:
        if arr[index] > arr[index-1] and arr[index] >= arr[index+1]:
            index2 = index+1
            while index2 < len(arr)-1:
                if arr[index2+1] > arr[index2]:
                    break
                index2 += 1
            if not(arr[index2] >= arr[index]):
                pos.append(index)
                peaks.append(arr[index])
            index = index2
        else:
            index += 1
    return {"pos": pos,  "peaks": peaks}
