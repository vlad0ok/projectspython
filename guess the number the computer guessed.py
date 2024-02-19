import random

choice_comp = random.randint(1, 10)
choice_pl = int(input("Enter number between 1 and 10: "))

if choice_comp == choice_pl:
    print(f"You win! The computer number was {choice_comp}")
else:
    print(f"You lose! The computer number was {choice_comp}")