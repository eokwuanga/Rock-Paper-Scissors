import random

game_over = False

while not game_over:

    user_action = input("Enter a choice (Rock=R, Paper=P, Scissors=S): ")

    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")

    if user_action == computer_action:
        game_over
        print(f"Both players selected {user_action}, It's a tie!, Try again!")

    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        break

    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        break

    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        break