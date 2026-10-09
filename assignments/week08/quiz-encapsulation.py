# Python Class Rectangle (by Nawpol Sanarnporn 6830252229)

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__length} length and {self.__width} width = {self.__length * self.__width}"

    def getPerimeter(self):
        return f"Perimeter of {self.__length} length and {self.__width} width = {2 * (self.__length + self.__width)}"

    def isSquare(self):
        return self.__length == self.__width

myRectangle = Rectangle(10,5)
myRectangle.__length = 100
print(myRectangle.getArea())
print(myRectangle.getPerimeter())
print(myRectangle.isSquare())