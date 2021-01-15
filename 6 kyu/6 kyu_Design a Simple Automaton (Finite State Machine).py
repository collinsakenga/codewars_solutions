class Automaton(object):

    def __init__(self):
        self.states = "q1"

    def read_commands(self, commands):
        for i in commands:
            if self.states=="q1":
                self.states="q1" if i=="0" else "q2"
            elif self.states=="q2":
                self.states="q3" if i=="0" else "q2"
            elif self.states=="q3":
                self.states="q2"
        return self.states=="q2"

my_automaton = Automaton()