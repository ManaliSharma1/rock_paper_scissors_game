import random
user_score = 0
computer_score = 0
while True:
    choices = ['Rock', 'Paper', 'Scissors']
    print("Choices are: ", choices)
    user_choice = input("Enter your choice: ")
    print("The users choice is: ", user_choice)
    print( )
    if user_choice not in choices:
        print("Please enter valid choice.")
        continue
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    print("The computer choice is: ", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
        print("You win !")
        user_score += 1
    else:
        print("Ohh! You lose.")
        computer_score += 1
    print( )
    print(f"Your score is {user_score}")
    print(f"Computer's score is {computer_score}")
    play_again = input("Do you want to play another round? (Yes/No) : ")
    if play_again == "No" or play_again == "no":
        break
    print( )
print("Thanks for playing.")

