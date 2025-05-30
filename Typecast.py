#Assigning different variables
name = "Sakura"
age = 23
is_student = False
weight = 54.9

# Prining different variables and their data type
print("Name: ", name)
print("Data Type of Name is: ", type(name))

print("Age: ", age)
print("Data Type of Age is: ", type(age))

print("is_student: ", is_student)
print("Data Type of is_student is: ", type(is_student))

print("weight: ", weight)
print("Data Type of weight is: ", type(weight))

#Typecasting of datatype to convert into variables
print("/n After Type Casting...")
age = str(age)
print(age)
print("Data Type of age is: ", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is: ", type(weight))

#Slicing
demo="I like coding"
print(demo[0:6:1])
print(demo[7::1])
print(demo[::-1])
