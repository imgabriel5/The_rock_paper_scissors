from random import randint

random_number = randint(1, 100)
i = 0
print("Zgadnij liczbę z przedziału 1 - 100")

chosen_number = 0
while chosen_number != random_number:
    i += 1
    chosen_number = int(input("Podaj liczbę: "))
    if chosen_number < random_number:
        print("Wylosowana liczba jest większa od Twojej")
    elif chosen_number > random_number:
        print("Wylosowana liczba jest mniejsza od Twojej")
    elif chosen_number == random_number:
        print(f"Gratulacje! Zgadłeś prawidłową liczbę i porzebowałeś do tego {i} prób/y!")