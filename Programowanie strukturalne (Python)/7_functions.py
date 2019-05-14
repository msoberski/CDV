def welcome():
    print('Hello', end=' ')
    print('Bob')

welcome()

def displayAge(age):
    print(f'Your age: {age}')

displayAge(20)

#Utwórz funkcję zwracającą iloczyn dwóch liczb. Użytkownik podaje dane z klawiatury.

def iloczyn(a, b):
    return a*b

first = float(input('Podaj pierwszą liczbę: '))
second = float(input('Podaj drugą liczbę: '))

print('Wynik mnożenia podanych liczb to:', iloczyn(first,second))

##############

def iloraz(a, b):
    return a/b

print('Iloraz wynosi:', iloraz(2, 4))
print('Iloraz wynosi:', iloraz(b=2, a=4))
