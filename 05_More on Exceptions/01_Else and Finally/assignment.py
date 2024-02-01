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