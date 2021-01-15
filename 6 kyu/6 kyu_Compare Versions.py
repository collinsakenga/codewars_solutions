def compare_versions(version1,version2):
    temp1=version1.split(".")
    temp2=version2.split(".")
    for i,j in zip(temp1, temp2):
        if int(i)>int(j):
            return True
        elif int(j)>int(i):
            return False
    return True if len(temp1)>=len(temp2) else False