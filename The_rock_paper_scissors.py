import random

options = ('rock', 'paper', 'scissors')
user_guesses = 0
computer_guesses = 0
print('Win 5 rounds to win the whole game!')

while True:
    random_element = random.choice(options)
    my_choice = input('Type rock, paper or scissors: ')
    if my_choice == 'paper' and random_element == 'rock' or \
            my_choice == 'rock' and random_element == 'scissors' or \
            my_choice == 'scissors' and random_element == 'paper':
        print(f'The computer has chosen: {random_element}')
        print('You have won the round with the computer!')
        user_guesses += 1
        if user_guesses == 5:
            print('Congratulations! You have won the game!')
            break
    elif my_choice == random_element:
        print(f'The computer has chosen: {random_element}')
        print('Draw! ')
    else:
        print('The computer has chosen:', random_element)
        print('The coumputer has won this round! ')
        computer_guesses += 1
        if computer_guesses == 5:
            print('Unfortunately, you have lost the game. Try again!')
            break