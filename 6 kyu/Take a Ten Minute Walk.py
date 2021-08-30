def is_valid_walk(walk):
    if len(walk)==10:
        if min(walk.count("n"),walk.count("s"))+min(walk.count("w"),walk.count("e"))==10/2:
            return True
    return False