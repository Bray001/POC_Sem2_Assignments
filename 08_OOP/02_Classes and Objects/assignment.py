<<<<<<< HEAD
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

=======
from math import hypot, atan, degrees, pi

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height   
        self.min_angle = atan(self.height / self.base)
        self.max_angle = pi / 2 - self.min_angle
        self.min_angle = degrees(self.min_angle)
        self.max_angle = degrees(self.max_angle)
        small = self.min_angle
        large = self.max_angle
        self.min_angle = min(small, large)
        self.max_angle = max(small, large)


    def area(self):
        # Youdo return the area which is 1/2 * base * height
        pass  # Remove this pass when finished
    
>>>>>>> 556b205ce2ccb6a118d333ff6fa171663eb03002
    def hypotenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
<<<<<<< HEAD
        return self.base + self.height + self.hypotenuse



triangle1 = RightTriangle(3,4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of Triangle1 is", triangle1.hypotenuse())
print("Angle 1 of triangle 1 is", triangle1.small_angle)
print("Angle 2 of triangle 1 is", triangle1.large_angle)
print("The perimeter of triangle1 is", triangle1.perimeter())
=======
        return self.base + self.height + self.hypotenuse()
    



triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of triangle1 is", triangle1.hypotenuse())
print("The perimeter of triangle1 is", triangle1.perimeter())
print("The small angle of triangle1 is", triangle1.min_angle)
print("The large angle of triangle1 is", triangle1.max_angle)

triangle2 = RightTriangle(30, 15)
print("The area of triangle2 is", triangle2.area())
print("The hypotenuse of triangle2 is", triangle2.hypotenuse())
print("The perimeter of triangle2 is", triangle2.perimeter())
print("The small angle of triangle2 is", triangle2.min_angle)
print("The large angle of triangle2 is", triangle2.max_angle)







# YOUDO: make another rightTriangle called triangle2
# YOUDO:  and print its area.
>>>>>>> 556b205ce2ccb6a118d333ff6fa171663eb03002
