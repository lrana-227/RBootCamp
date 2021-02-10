# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors! There are three trys!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
for x in range(3):
    computer_choice = random.choice(options)

# User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    print(f"The computer chose {computer_choice}")


    computer_wins = 0
    you_wins = 0
# Run Conditionals

    if ((user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r")):
        print("The computer won this round")
        computer_wins=computer_wins+1
    elif ((user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p") ):
        print("You won this round!")
        you_wins=you_wins+1
    elif ((user_choice == "s" and computer_choice == "s")or (user_choice == "s" and computer_choice == "s") or (user_choice == "s" and computer_choice == "s")):
        print("You and the computer picked the same value. No one gets points")
    else: 
        print("You entered an invalid option")
        print("You both gain no points and loose a turn")


if computer_wins>you_wins:
    print("The computer won :(")
elif computer_wins<you_wins:
    print("YOU WON!!! YAY!!! :)")
else:
    print("You both tied in points---- you both can't type or can read each others mind!")