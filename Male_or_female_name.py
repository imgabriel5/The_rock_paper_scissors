# Czy podano imię męskie czy żeńskie?
name = input('Podaj imię: ')
gender = 'Podano imię męskie.' if name[-1] != 'a' or name == 'Kuba' else 'Podano imię żeńskie.'
print(gender)
print('----------------------------------------------------------------------------------------------------------')
# Więcej imion.
names = ['Adam', 'Alina', 'Grzegorz', 'Kamil', 'Kuba']
males = []
for name in names:
    if name [-1] != 'a' or name == 'Kuba':
        males.append(name)

print(f'Mężczyźni z tego zestawu mają na imię: {males}.')
print('----------------------------------------------------------------------------------------------------------')
# Dodanie zwrotu 'Pan/i' do odpowiedniej osoby.
ladies = [name for name in names if name [-1] != 'a' or name == 'Kuba']
print('Names:', names)
print("Male's names:", ladies)
names = ['Adam', 'Alina', 'Grzegorz', 'Kamil', 'Malgorzata']
formal = [f'Pani {name}' if name[-1] == 'a' else f'Pan {name}' for name in names]
print(formal)