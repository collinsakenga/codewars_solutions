def grille(message, code):
    if not message:
        return ""
    binary = bin(code)[2:]
    if len(binary) <= len(message):
        binary = binary.zfill(len(message))
        return "".join(message[i] for i, j in enumerate(binary) if j == "1")
    return "".join(message[i] for i, j in enumerate(binary[-len(message):]) if j == "1")
