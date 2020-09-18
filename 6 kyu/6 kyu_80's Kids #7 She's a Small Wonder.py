class Robot:
    def __init__(self):
        self.record = {"do", "not", "thank", "you", "for", "teaching", "me",
                       "i", "already", "know", "the", "input", "understand", "word"}

    def learn_word(self, s):
        if not s:
            return "I do not understand the input"
        for i in s:
            if not i.isalpha():
                return "I do not understand the input"
        if s.lower() in self.record:
            return f"I already know the word {s}"
        self.record.add(s.lower())
        return f"Thank you for teaching me {s}"
