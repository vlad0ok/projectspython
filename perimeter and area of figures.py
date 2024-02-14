import math

class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return f"Perimeter of your rectangle: {2 * (self.a + self.b)}"

    def square(self):
        return f"Square of your rectangle: {(self.a * self.b)}"


class Triangle():
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def perimeter(self):
        return f"Perimeter of your triangle: {self.a + self.b + self.c}"

    def square(self):
        return f"Square of your triangle: {(self.a * self.h)/2}"


class Cube():
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return f"Perimeter of your cube: {self.a * 4}"

    def square(self):
        return f"Square of your cube: {(self.a * self.a)}"

class Circle():
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return f"Perimeter of your circle: {2*math.pi*self.r}"

    def square(self):
        return f"Square of your circle: {math.pi*self.r**2}"






wh_f = input("Enter your figure(rectangle - r, triangle - t, cube - c or circle - ci): ")
if wh_f == 'r':
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    rectangle = Rectangle(a, b)
    print(rectangle.perimeter())
    print(rectangle.square())
elif wh_f == 't':
    a = int(input("Enter the base of the triangle: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    h = int(input("Enter the height of the triangle: "))
    triangle = Triangle(a, b, c, h)
    print(triangle.perimeter())
    print(triangle.square())
elif wh_f == 'c':
    a = int(input("Enter side of cube: "))
    cube = Cube(a)
    print(cube.perimeter())
    print(cube.square())
elif wh_f == 'ci':
    r = int(input("Enter radius of circle: "))
    circle = Circle(r)
    print(circle.perimeter())
    print(circle.square())