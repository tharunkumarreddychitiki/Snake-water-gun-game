# random module is imported to generate a random interger.
import random
import time
num = random.randint(1,3) # generates a random interger between 1 and 3.

name = input("Enter your name : ")
print(f"Hi {name}!\nWelcome to the game : Snake Water Gun.\nThis is just a game that is simlar to rock paper scissors.\nTry your luck with the computer")

#Asks the user to enter their choice.
choice = int(input("1. Snake\n2. Water\n3. Gun\nEnter your choice : "))
#Print the choice of the computer.
if num == 1 :
    print("1. Snake")
else :
    print("2. Water") if num == 2 else print("3. Gun")

#Prints if you loose or win or it's a draw 
if (choice == 1 and num == 1) or (choice == 2 and num == 2) or (choice == 3 and num == 3) :
    print("It's a Draw!!")

elif (choice == 1 and num == 2) or (choice == 2 and num == 3) or (choice == 3 and num == 1) :
    print("You win!!")

elif(choice == 1 and num == 3) or (choice == 2 and num == 1) or (choice == 3 and num == 2) :
    print("You Lose!!")