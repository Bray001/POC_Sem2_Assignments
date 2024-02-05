<<<<<<< HEAD
Number1 = 0
Number2 = 0
try:

    Number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))
except ValueError:
    print("integer wasnt giver")
else:
    print("No value error detected")
finally:
    print("values taken care of")

try:
    answer = Number1/Number2

except ZeroDivisionError:
    print("divide by 0 is not possible")
=======
#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    # YOUDO.  use input function and int to set number2
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    # YOUDO divide number1 / number2 and set to answer
    # YOUDO  print the result of the division (aka answer with some helper text)
    pass  # YOUDO remove pass when done
except ZeroDivisionError:
    # YOUDO:  print message stating that division by zero is not possible.
    pass  # YOUDO remove pass when done
#YOUDO:  else and finally here as well.  
>>>>>>> ce1c232a42c72d8fe1a834e43f345162e2f81fa4
