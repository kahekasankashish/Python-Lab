# Q2. Define a class Box with basic data members and member functions. Create Box objects and compute their volumes.
class Box:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

box1 = Box(10, 20, 5)
print("Volume =", box1.volume())
