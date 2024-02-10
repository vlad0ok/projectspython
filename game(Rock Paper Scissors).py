import random

eq = ["rock", "paper", "scissors"]
your_choice = input("Enter rock, paper or scissors?: ")
bot = random.choice(eq)
if your_choice == bot:
    print(f"Game draw! you have '{your_choice}' and '{bot}'")
elif your_choice == 'rock' and bot == 'paper':
    print(f"Bot win! Bots bet was '{bot}'")
elif your_choice == 'rock' and bot == 'scissors':
    print(f"You win! Bots bet was '{bot}'")
elif your_choice == 'paper' and bot == 'rock':
    print(f"You win! Bots bet was '{bot}'")
elif your_choice == 'paper' and bot == 'scissors':
    print(f"Bot win! Bots bet was '{bot}'")
elif your_choice == 'scissors' and bot == 'paper':
    print(f"You win! Bots bet was '{bot}'")
elif your_choice == 'scissors' and bot == 'rock':
    print(f"Bot win! Bots bet was '{bot}'")