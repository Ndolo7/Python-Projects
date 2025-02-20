import random


ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {
    ROCK:'🪨',
    PAPER:'📄',
    SCISSORS:'✂️'
}
choices = tuple(emojis.keys()) #tuple, which is read only

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice')

def display_choices(user_choice, comp_choice):
    print(f'you chose {emojis[user_choice]}')
    print(f'the computer chose {emojis[comp_choice]}')

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print('Tie')

    elif (
        (user_choice == ROCK and comp_choice == SCISSORS) or 
        (user_choice == PAPER and comp_choice == ROCK) or 
        (user_choice == SCISSORS and comp_choice == PAPER)
    ):
        print('You Win!')
        

    elif (
        (user_choice == ROCK and comp_choice == PAPER) or 
        (user_choice == PAPER and comp_choice == SCISSORS) or 
        (user_choice == SCISSORS and comp_choice == ROCK)
    ):
        print('You Lose!')


def play_game():
    while True:
        user_choice = get_user_choice()
        comp_choice = random.choice(choices)
        
        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)    

        should_continue = input('Do you want to continue? (y/n)').lower()

        if should_continue != 'y' and should_continue != 'n':
            print('Invalid choice')
            break
        elif should_continue == 'n':
            print('Good bye')
            break
        else:
            continue


play_game()

