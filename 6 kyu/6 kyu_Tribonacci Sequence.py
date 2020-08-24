def tribonacci(signature, n):
    total = 0
    if n < 4:
        return signature[0:n]
    for num in signature:
        total += num
    signature.append(total)
    index = 1
    while len(signature) < n:
        temp = total+signature[index]+signature[index+1]
        num = total
        total = temp
        signature.append(temp)
        index += 1
    return signature
