def Hangman(guess, word):
    table={i:i for i in guess.lower()}
    return "".join(table.get(i, "_") for i in word.lower())