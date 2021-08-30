def string_slicer(string, size):
    return [string[i:i+size] for i in range(0, len(string), size)]