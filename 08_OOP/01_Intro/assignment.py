class RightTriangle:
<<<<<<< HEAD
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
=======
    def __init__(self, base, height):
        self.base = base
        #YOUDO:  do the same for height
    
    def area(self):
        #Youdo return the area which is 1/2 * base * height
        pass #Remove this pass when finished

triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())

#YOUDO: make another rightTriangle called triangle2
#YOUDO:  and print its area.  

>>>>>>> 37cad7e71375968e8aa8a2c2a7a5885707699985
