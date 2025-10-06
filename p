# # Class creation
# class myClass:
#     __privateVar = 27;

#     def __privMeth(self):
#         print("I'm inside class myClass")
#     def hello(self):
#         print("Private Variable value:",myClass.__privateVar)

# foo = myClass()
# foo.hello()
# foo.__privMeth

#Encapsulation

class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(3000)
c.sell()

#point function
class Point:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return"({0}, {1})".format(self.x, self.y)
    
p1 = Point(9,7)
print(p1)
