#take input from user
rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0: #conditions
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow - 1
#loop for upper part
for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space=space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space = 1
#loop for lower part
for i in range(1, halfDiamRow):
    for j in range(1, space+1):
        print(end=" ")
    space=space+1
    num = 1
    for j in range(1, 2*(halfDiamRow-i)):
        print(end=str(num))
        num=num+1
    print()