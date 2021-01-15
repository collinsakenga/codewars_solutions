def morse_converter(string):
    dict={'.----': 1, '..---': 2, '...--': 3, '....-': 4, '.....': 5, '-....': 6, '--...': 7, '---..': 8, '----.': 9, '-----': 0}
    return int("".join(str(dict[string[i:i+5]]) for i in range(0, len(string), 5)))