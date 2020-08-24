def generate_hashtag(s):
    # return False if the precondition is not met
    if len(s) > 140 or len(s) == 0:
        return False
    # Add first letter of result, "#"
    result = "#"
    for word in s.split():
        # capitalize the first letter of word in the list
        word = word.capitalize()
        # append result
        result += word
    return result
