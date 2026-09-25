"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

import math


class Shape:

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

"""
สร้างคลาส Circle ที่ประยุกต์ใช้คลาส

"""

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius


rect = Rectangle(10, 5)
my_circle = Circle(7)

print(rect.get_area())
print(rect.get_perimeter())

print(f"Rectangle Area: {rect.get_area()}")
print(f"Circle Area: {my_circle.get_area():.2f}")
print(
    f"Circle Perimeter: {my_circle.get_perimeter():.2f}"
)