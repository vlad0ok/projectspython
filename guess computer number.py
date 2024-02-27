import random

comp = random.randint(1, 15)
while True:
    user = int(input("Enter a number from 1 to 15: "))
    if user == comp:
        print(f"You win! Computer number was {comp}")
        break
    elif user > comp:
        print("No! Computer number is less than yours.")
    elif user < comp:
        print("No! Computer number is greater than yours.")
