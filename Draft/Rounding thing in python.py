def typing_test(seconds,sentence):
    return f"{round(len(sentence.split())*60/seconds+0.0000001)} WPM"