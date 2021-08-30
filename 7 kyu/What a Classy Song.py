class Song():
    def __init__(self, title, artist):
        self.title=title
        self.artist=artist
        self.arr=set()
    def how_many(self, arr):
        length=len(self.arr)
        for i in arr:
            self.arr.add(i.lower())
        return len(self.arr)-length