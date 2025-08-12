import random
roll = random.randint(1, 6)
guess = int(input("Guess the dice roll (1-6): "))
if guess == roll:
    print("You guessed it right!")
else:
    print("Wrong guess!")
print(f"The computer rolled a {roll}")