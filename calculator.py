def add(x, y):
    return x+y
def substract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

print("Please select which calculation you want to do!")
print("i. Add")
print("ii. Substract")
print("iii. Multiply")
print("iv. Divide")

choice = input("Please enter choice(i/ii/iii/iv): ")

num_1 = int(input("Enter the first number you want to input: "))
num_2 = int(input("Enter the second number you want to input: "))

if choice == "i":
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == "ii":
    print(num_1, "-", num_2, "=", substract(num_1, num_2))
elif choice == "iii":
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == "iv":
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is an invalid input")