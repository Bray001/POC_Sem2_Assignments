class RightTriangle:
    def _init_(self,base, height):
        self.base = base
        self.height = height

    
    def area(self):
        return 0.5 * self.base * self.height
    


tri1 = RightTriangle(3,4)
print("The base of the tril is", tri1.base)
print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area)

tri2 = RightTriangle(2, 6)


print("The base of the tri2 is", tri2.base)
print("The height of tri2 is", tri2.height)
print("The area of tri2 is", tri2.area)
