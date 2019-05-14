x = 5
if x == 5:
    print('x jest rowne 5')
    print(f'x = {x}')
else:
    print(f'x jest rowne {x}')
print('Za instrukcją warunkową')

################

y = True #False

if y: #y == true
    print('Prawda')
else:
    print('True')

################

z = 5 > 6

if z:
    print('p')
else:
    print('f')

################

j = '1'
j = '0'
j = ''

if bool(j):
    print(1)
else:
    print(0)

################

k = input('Podaj k: ')
if bool(k):
    print('Zmienna k zawiera dane')
else:
    print('Zmienna k nie zawiera danych')
