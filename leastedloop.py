#loop
i=1#intialise
while i<=10:
    j=1
    while j<=10:
        print(j,end="")
        j=j+1
    i=i+1
    print()

#take input of a word
string = input("Enter your word: ")
#take input of a character
char = input("Please enter your own character: ")
i = 0
count = 0
while(i < len(string)):#string operation
    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1

 #display the result
print("The total number of times" , char, "has occured =" , count )

num=int(input("Enter your number: "))
for i in range(2,num):
    if num%i==0:
        print("Number is not prime")
        break
else:
        print("Number is prime")
