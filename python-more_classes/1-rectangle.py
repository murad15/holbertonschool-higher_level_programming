#!/usr/bin/python3
'''Rectangle class defines rectangle'''


class Rectangle:
    '''Rectangle class defines rectangle'''

    def __init__(self, width=0, height=0):
        '''Instnciate the parameters'''

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Property getter'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Property setter'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''Property getter'''

        return self.__width

    @height.setter
    def height(self, value):
        '''Property setter'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
