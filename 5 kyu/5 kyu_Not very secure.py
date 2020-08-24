def alphanumeric(password):
    if not password:
        return False
    for char in set(password):
        if not char.isalnum():
            return False
    return True
x