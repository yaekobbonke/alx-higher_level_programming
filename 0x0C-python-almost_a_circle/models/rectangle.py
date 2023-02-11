#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width (self):
        return sef.__width
    @width.setter
    def width(self, n):
        if type(n) is not int:
            raise TypeError("width must be an integer")
        if n <= 0:
            raise ValueError("width must be > 0")
        self.__width = n
    @property
    def height (self):
        return self.__height
    @height.setter
    def height (self, m):
        if type(m) is not int:
            raise TypeError("Height must be an integer")
        if m <= 0:
            raise ValueError("height must be > 0")
        self.__height = m

    @property
    def x (self):
        return self.__x
    @x.setter
    def x(self, a):
        if type(a) is not int:
            raise TypeError("x must be an integer")
        if a < 0:
            raise ValueError("x must be >= 0")
        self.__x = a
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, b):
        if type(b) is not int:
            raise TypeError("y must be an integer")
        if b < 0:
            raise ValueError("y must be >= 0")
        self.__x = b
    def area(self):
        return self.__width*self.__height


