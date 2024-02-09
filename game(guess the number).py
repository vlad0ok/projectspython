import random

name = str(input("Enter your name: "))
choice = int(input("Enter number from 1 to 10: "))
rand = random.randint(1, 10)
if choice == rand:
    print(f"{name}, you win!, my number was too {rand}")
elif choice != rand:
    print(f"{name}, you lose, LOSER!. My number was {rand}")
else:
    print("Error")