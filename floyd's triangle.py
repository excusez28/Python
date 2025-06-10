#take input from user
rows = int(input("Please enter the number of rows: "))
number = 1 #intialise by 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows+1):
    #inner loop for numbers of columns
        for j in range(1, i+1):
                print(number, end=' ')
                number=number+1
        print()