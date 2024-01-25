try:
    value1 = int(input("Enter an intender:"))
    value2 = int(input("enter another integer:"))
    print("The answer is", value1/value2)
except ZeroDivisionError:
    print("you provide 0 and division by 0 is not possible, sorry.")