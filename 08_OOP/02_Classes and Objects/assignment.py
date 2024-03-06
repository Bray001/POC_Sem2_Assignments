from math import hypot, atan, degrees, min, max

class RightTriangle:
    def _init_(self, base, height):
        self.base = base
        self.height = height
        self.angle1 = atan(self. height / self.base)
        self.angle2 = atan( self.base / self.height)
        self.angle2 = degrees(self.large_angle)
    
    def area(self):
        return 0.5 * self.base * self.height

    def hypotenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse



triangle1 = RightTriangle(3,4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of Triangle1 is", triangle1.hypotenuse())
print("Angle 1 of triangle 1 is", triangle1.small_angle)
print("Angle 2 of triangle 1 is", triangle1.large_angle)
print("The perimeter of triangle1 is", triangle1.perimeter())