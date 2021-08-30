class add(int):
    def __call__(self, func):
        return add(self+func)