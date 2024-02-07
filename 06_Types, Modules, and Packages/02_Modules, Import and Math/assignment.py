import math
number1 = float(input("enter a number: "))
number2 = float(input("Enter number 2: "))

leg1 = number1
leg2 = number2

hyp=math.hypot(leg1, leg2)

print("the hypotenuse is", hyp)