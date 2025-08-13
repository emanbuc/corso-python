import random
player1 = input("Enter name for Player 1: ")
print(f"Player 1: {player1}")
player2 = input("Enter name for Player 2: ")
print(f"Player 2: {player2}")
print("Game setup complete. Players are ready to start the game!")



def roll_dice():
    dice_total= random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def determine_winner(roll1, roll2):
    if roll1 > roll2:
        return player1
    elif roll2 > roll1:
        return player2
    else:
        return "It's a tie!"    
def main():
    roll1 = roll_dice()
    roll2 = roll_dice()
    winner = determine_winner(roll1, roll2)
    print(f"{player1} rolled a total of {roll1}")
    print(f"{player2} rolled a total of {roll2}")
    print(f"The winner is: {winner}")

if __name__ == "__main__":
    main()
