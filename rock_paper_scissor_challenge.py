import random
import rock_paper_scissors_ascii_arts

while True:
    try:

        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        rock_paper_scissor_list = [rock_paper_scissors_ascii_arts.rock, rock_paper_scissors_ascii_arts.paper, rock_paper_scissors_ascii_arts.scissors]

        print(rock_paper_scissor_list[player_choice])

        print("Computer choose:")

        computer_choice = random.randint(0, 2)

        print(rock_paper_scissor_list[computer_choice])

        if player_choice == 0:
            if computer_choice == 0:
                print("Draw!")
            elif computer_choice == 1:
                print("You lose!")
            else:
                print("You win!")
        elif player_choice == 1:
            if computer_choice == 1:
                print("Draw!")
            elif computer_choice == 0:
                print("You win!")
            else:
                print("You lose!")
        else:
            if computer_choice == 2:
                print("Draw!")
            elif computer_choice == 0:
                print("You lose!")
            else:
                print("You win!")

        break

    except:

        print("Please enter valid numbers")
