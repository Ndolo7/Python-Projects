import random

while True:
    choice = input('Roll the Dice (y/n)?').lower()
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if choice == 'y':
        print(f"({die1}, {die2})")
    elif choice == "n":
        print('Thank you for playing')
    else:
        print('Invalid Input!')
            