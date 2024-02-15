import random

cards = [6, 7, 8, 9, 10, 2, 3, 4, 11]
dealer = random.randint(15, 21)
random.shuffle(cards)
count = []

while True:
    num = random.choice(cards)
    count.append(num)
    print(f"You have: {sum(count)}")

    if sum(count) > 21:
        print(f"You lose! You have {sum(count)}")
        break
    elif sum(count) == 21:
        print(f"You win! You have {sum(count)}")
        break

    choice = input("Will you take the card? (y/n): ")
    if choice.lower() != 'y':
        player_total = sum(count)
        print(f"Your final total is: {player_total} and dealer has {dealer}")
        if player_total > dealer:
            print("Congratulations! You win!")
        elif player_total < dealer:
            print("Sorry, you lose!")
        else:
            print("It's a tie!")
        break


