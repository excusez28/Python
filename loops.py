#input integer value
n = int(input("Enter the number whose sum you want to find: "))
sum=0

#iterates for n+1 time: i+1 to n+1
for i in range(1, n+1):
    sum = sum+i
print("\nSum =" , sum)

#Input a word or sentence
string = input("Please eneter your own string: ")

string2 = ('')
#loop for printing in reverse
for i in string: 
    string2 = i + string2

print("\nThe Orginal String=", string)
print("The Reversed String=", string2)

for i in range(10,0,-1):
    print(i)