#count the notes
#Taking total amount as input from user
Amount = int(input("Please enter amount for withdraw: "))

#Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 rupee", note_1)
print("notes of 50 rupee", note_2)
print("notes of 10 rupee", note_3)

#Percentage Calculation
print("Enter marks otained in 4 subjects: ")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
bgs = int(input("bgs: "))

#Lets calculate the percentage of marks
sum = math+english+science+bgs
print("sum of math,english,science,bgs")

perc = (sum/400)*100

print(end="Percentage Marks=")
print(perc)