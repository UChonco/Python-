import random 

option = ("rock", "paper", "scissors")

computer = random.choice(option)    

while True:
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    if player == computer:
        print(f"It's a tie! You both chose {player}.")
    elif player == "rock" and computer == "scissors":
        print("You win")
        break
    elif player == "scissors" and computer == "paper":
        print("You win")
        break
    elif player == "paper" and computer == "rock":
        print("You win")
        break
    else:
        print("You lose")

