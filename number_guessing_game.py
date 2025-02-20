import random

num = random.randrange(100) #or use randint(1, 100)

while True:
    try:
        choice = int(input('Guess the number between 1 and 100: '))
        if choice > num and 1 < choice < 100:
            print('Too high')
        elif choice < num and 1 < choice < 100:
            print('Too low!')
        elif choice == num:
            print('Congratulations! You made the right guess')
            print(f'The answer is {num}')
            break
        else:
            print('Invalid input')
    except ValueError:
        print('Please enter a valid number')

