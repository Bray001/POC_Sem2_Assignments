class Rectangle:
    
    counter = 0

    def get_count():
        return Rectangle._counter
    
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height

     def get_base(self) -> float:
        return self.__base
    
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
 
 rectangle1 = Rectangle (4,3) 
print("the base of rectangle is", rectangle1.get_base)
print("the height of rectangle is", rectangle1.get_height)
print("The perimeter is", rectangle1.get_perimeter)
print("The area of rectange is", rectangle1.get_area.)

rectangle2 = Rectangle (2,5)
print("the base of rectangle is", rectangle2.get_base)
print("the height of rectangle is", rectangle2.get_height)
print("The perimeter is", rectangle2.get_perimeter)
print("The area of rectange is", rectangle2.get_area.)


 
 
#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
