def duplicate_count(text):
    total = 0
    text = text.lower()
    for char in set(text):
        if text.count(char) > 1:
            total += 1
    return total
