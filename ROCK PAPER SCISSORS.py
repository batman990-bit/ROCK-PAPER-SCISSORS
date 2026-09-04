
import random

print("ROCK PAPER SCISSORS ")
print("=========================")

choices = ["rock", "paper", "scissors"]


player_score = 0
computer_score = 0
ties = 0




while True:
    player = input("\nChoose Rock, Paper, or Scissors\n(or type 'quit' to exit): ").lower()
    
    if player == "quit":
        print("\n" + "=" * 30)
        print(" FINAL SCOREBOARD")
        print(f"You: {player_score} | Computer: {computer_score} | Ties: {ties}")
        
        if player_score > computer_score:
            print("Victory! You destroyed the bot!")
        elif computer_score > player_score:
            print("The machines are taking over... better luck next time!")
        else:
            print("It's a total dead heat!")
            
        print("Thanks for playing!")
        break
        
    if player not in choices:
        print("\nOops! That's not a valid choice. Try again.")
        print("-" * 30)
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")



    
    if player == computer:
        print(f"It's a Draw! Both chose {player}")
        ties += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print(f"You Win! {player} beats {computer}")
        player_score += 1
    else:
        print(f"Computer Wins! {computer} beats {player}")
        computer_score += 1
        

    
    print("\n SCOREBOARD")
    print(f"Player: {player_score}  | Computer: {computer_score}  | Ties: {ties}")
    print("-" * 30)