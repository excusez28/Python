import random
playing = True
number = str(random.randint(34,67))

print("We will play a number game today where you have to guess a number from 34 to 67")
print("The game ends when the number match")
while playing:
    guess = input("Input your best guess :")
    if number == guess:
        print("You are the winner!")
        print("The number was",number)
        break

    else:
        print("You guess number is incorrect. Try again!!")