def will_fit(present, box):
    present = sorted(present)
    box = sorted(box)
    for i in range(len(present)):
        if box[i]-present[i] < 2:
            return False
    return True
