# # Przykładowy test.
# def add_numbers(a:int, b:int) -> int:
#     return a + b
#
# def test_add_numbers(): # Tutaj rozpoczyna się test.
# # given - to też czasami pojawia się w kodzie.
#     a = 2
#     b = 3
# # when (określa to, co się zadziało)
#     value = add_numbers(a, b)
#
#     assert value == 5 # To co po assercie i to co w testowanym kodzie będzie prawdą, to test zapali się na zielono.
#                       # Poniżej możemy dodać jeszcze więcej assertów.
########################################################################################### ZADANIE
# Przygotuj funkcję, która zliczy ilość znaków w tekście zawierających się wewnątrz nawiasów okrągłych. Nawiasy mogą
# występować w tekście wielokrotnie, nigdy nie będą się w sobie zawierać.
import pytest

def count_chars_between(text: str, char_start: str = '(', char_end: str = ')'):
    # Zmienna boolowska, która określa, czy powinniśmy liczyć znaki
    should_count_char = False
    # Zmienna do przechowywania liczby znaków
    counter = 0

    # Iterujemy przez każdy znak w tekście
    for char in text:
        # Jeśli znak jest znakiem końcowym, zatrzymujemy liczenie znaków
        if char == char_end:
            should_count_char = False

        # Jeśli powinniśmy liczyć znaki, inkrementujemy licznik
        if should_count_char:
            counter += 1

        # Jeśli znak jest znakiem początkowym, rozpoczynamy liczenie znaków
        if char == char_start:
            should_count_char = True

    # Zwracamy wynik liczenia znaków
    return counter

# Test 1
assert count_chars_between("Hello (world)!") == 5
# Sprawdza, czy funkcja poprawnie zlicza znaki między nawiasami

# # Test 2
# assert count_chars_between("{count the characters}", char_start='{', char_end='}') == 20
# # Sprawdza, czy funkcja poprawnie zlicza znaki między nawiasami klamrowymi
#
# # Test 3
# assert count_chars_between("[count the characters]", char_start='[', char_end=']') == 20
# # Sprawdza, czy funkcja poprawnie zlicza znaki między nawiasami kwadratowymi
#
# # Test 4
# assert count_chars_between("No characters to count.") == 0
# # Sprawdza, czy funkcja poprawnie zwraca 0, gdy nie ma znaków do zliczenia
#
# # Test 5
# assert count_chars_between("(count only the characters) between these brackets", char_start='(', char_end=')') == 25
# # Sprawdza, czy funkcja poprawnie zlicza znaki między wybranymi nawiasami