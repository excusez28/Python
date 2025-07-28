import random

options = ["Rock","Paper","Scissors"]

user_choice = input("Choose rock, paper or scissors: ")

computer_choice = random.choice(options)

print("You chose", user_choice)
print("Computer chose", computer_choice)

if user_choice == computer_choice:
    print("Its a tie")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors, YOU WIN!!")
elif user_choice == "Papr" and computer_choice == "Rock":
    print("Paper covers Rock, YOU WIN!!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut Paper, YOU WIN!!")
else:
    print("You lose!")