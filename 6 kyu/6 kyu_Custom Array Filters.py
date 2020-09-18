class list:
    def __init__(self, list):
        self.list = list

    def even(self):
        return [i for i in self.list if isinstance(i, int) and i % 2 == 0]

    def odd(self):
        return [i for i in self.list if isinstance(i, int) and i % 2 == 1]

    def under(self, limit):
        return [i for i in self.list if isinstance(i, int) and i < limit]

    def over(self, limit):
        return [i for i in self.list if isinstance(i, int) and i > limit]

    def in_range(self, down, up):
        return [i for i in self.list if isinstance(i, int) and (i >= down and i <= up)]
