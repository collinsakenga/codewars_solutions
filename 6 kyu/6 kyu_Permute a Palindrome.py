def permute_a_palindrome(input):
    count = 0
    for i in set(input):
        if input.count(i) % 2 != 0:
            count += 1
    return True if count <= 1 else False
