def happy_or_sad(face):
    return "sad" if any(i for i in "([" if i in face) else "happy"