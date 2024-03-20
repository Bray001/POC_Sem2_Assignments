class Rectangle:
<<<<<<< HEAD

=======
>>>>>>> 329e22c338e86f7ca64a1003376386ff823260c7
    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
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
<<<<<<< HEAD
        return 2 * self.__base + 2 * self.__height

    
    def __str__(self) -> str:
        pass

class Square(Rectangle):
    def __init__(self, side_length:float) -> None:
        super().__init__(side_length, side_length)
        self.__side_length = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def __str__(self) -> str:
        return " square with side length:" + str(self.__side_length)



square1 = Square(3)
print(square1)
print("The base of square1 is", square1.get_base())
print("the height of square1 is", square1.get_height())
print("The side length of square1 is", square1.get_side_length())
print("The area of square1 is", square1.get_area())
print("The perimeter of square1 is", square1.get_perimeter())
=======
        return self.__base * self.__height

    def __str__(self) -> str:
        # Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)
    
class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.__side = side
        
    def get_side(self) -> float:
        return self.__side
    
    def __str__(self) -> str:
        # Square with side:3
        return "Square with side:" + str(self.__side)
    
square1 = Square(3)
print(square1)
print("The side of square1 is", square1.get_side())
print("The perimeter of square1 is", square1.get_perimeter())
print("The area of square1 is", square1.get_area())
print()
rectangle1 = Rectangle(3, 4)
print(rectangle1)
print("The base of rectangle1 is", square1.get_base())
print("The height of rectangle1 is", square1.get_height())
print("The perimeter of squarectangle1re1 is", square1.get_perimeter())
print("The area of rectangle1 is", square1.get_area())
>>>>>>> 329e22c338e86f7ca64a1003376386ff823260c7
