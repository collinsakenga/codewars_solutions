def music(numbers):
    s="Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you".split("\n")
    return [s[val].replace("Never gonna", "NEVER GONNA") if index%2 else s[val] for index, val in enumerate(numbers)]