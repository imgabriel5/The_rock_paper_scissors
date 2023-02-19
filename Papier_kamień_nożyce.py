import random

options = ('papier', 'kamień', 'nożyce')
user_guesses = 0
computer_guesses = 0
print('Wygraj 5 razy z komputerem, aby móc wygrać całą grę!')

while True:
    random_element = random.choice(options)
    my_choice = input('Wybierz papier, kamień lub nożyce: ')
    if my_choice == 'papier' and random_element == 'kamień' or \
            my_choice == 'kamień' and random_element == 'nożyce' or \
            my_choice == 'nożyce' and random_element == 'papier':
        print(f'Komputer wylosował: {random_element}')
        print('WYGRAŁEŚ Z KOMPUTEREM!')
        user_guesses += 1
        if user_guesses == 5:
            print("Koniec! Wygrałeś całą grę!")
            break
    elif my_choice == random_element:
        print(f'Komputer wylosował: {random_element}')
        print('REMIS! ')
    else:
        print('Komputer wylosował:', random_element)
        print('KOMPUTER WYGRAŁ Z TOBĄ! ')
        computer_guesses += 1
        if computer_guesses == 5:
            print("Niestety, ale przegrałeś całą z komputerem. Spróbuj ponownie!")
            break