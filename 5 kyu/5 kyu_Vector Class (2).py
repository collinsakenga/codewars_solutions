class Vector:
    def __init__(self, vector, j=None, k=None):
        self.vector = [vector, j, k] if (j and k) else vector

    def __add__(self, vector):
        return Vector([self.x+vector.x, self.y+vector.y, self.z+vector.z])

    def __sub__(self, vector):
        return Vector([self.x-vector.x, self.y-vector.y, self.z-vector.z])

    def __eq__(self, other):
        return self.vector == other.vector

    def cross(self, vector):
        return Vector([self.y * vector.z - self.z * vector.y, self.z * vector.x - self.x * vector.z, self.x * vector.y - self.y * vector.x, ])

    def dot(self, vector):
        return self.x*vector.x+self.y*vector.y+self.z*vector.z

    def to_tuple(self):
        return tuple(self.vector)

    def __str__(self):
        return "<"+", ".join(str(i) for i in self.vector)+">"

    def get_x(self):
        return self.vector[0]

    def get_y(self):
        return self.vector[1]

    def get_z(self):
        return self.vector[2]

    def get_magnitude(self):
        return sum(i**2 for i in self.vector)**0.5
    magnitude = property(get_magnitude)
    x = property(get_x)
    y = property(get_y)
    z = property(get_z)
