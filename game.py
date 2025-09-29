import random
options = ["rock", "paper", "scissors"]
while True:
    computer_choice = random.choice(options)
    try:
        user_choice = str(input("rock, paper or scissors?(ctrl + c to stop)").lower())
    except KeyboardInterrupt:
        break
    else:
        if computer_choice == user_choice:
            print(f"Computer chose {computer_choice}, you chose {user_choice}. Draw!")
        elif (computer_choice == "rock" and user_choice == "scissors") or (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper"):
            print(f"Computer chose {computer_choice}, you chose {user_choice}. Computer Wins")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print(f"Computer chose {computer_choice}, you chose {user_choice}. Congarts, you win!!")
        