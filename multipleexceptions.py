try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by Zero is error!!")

except SyntaxError:
    print("comma is missing, Enter number separated like this 1,2")

except:
    print("wrong input")

else:
    print("No exceptions")

finally:
    print("This will excute no matter what")