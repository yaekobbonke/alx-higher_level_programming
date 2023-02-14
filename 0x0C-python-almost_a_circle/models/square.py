#!/usr/bin/python3

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, id, x, y, width, height):
        self.size = width
        self.size = height
    def __str__(self):
        return [Square] '{:d} {:d}/{:d} - <size>'.format(self.id, self.x, self.y)
