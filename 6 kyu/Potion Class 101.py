from math import ceil
class Potion:
    def __init__(self, color, volume):
        self.red=color[0]*volume
        self.green=color[1]*volume
        self.blue=color[2]*volume
        self.volume=volume
        self.color=color
    def mix(self, other):
        temp1=self.red+other.red
        temp2=self.green+other.green
        temp3=self.blue+other.blue
        temp4=self.volume+other.volume
        return Potion((ceil(temp1/temp4), ceil(temp2/temp4), ceil(temp3/temp4)), temp4)