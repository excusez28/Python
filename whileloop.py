#Sum of natural numbers
#Input the value of terms
n = int(input("Enter the value of terms: "))
sum = 0 #intialise
i = 1 #intialise
while i<=n: #loop will run 1 to n
    sum=sum+i
    i=i+1

print("/nSum=" , sum)

# #Infinity
# i=0
# while i<=0:
#     print("Waterlily is the national flower of Bangladesh")

#take input from the user
num = int(input("Enter a number: "))

#Intialize sum
sum = 0

#find the sun of the cube of the each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

#Display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")