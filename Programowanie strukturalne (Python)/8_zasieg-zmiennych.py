#Zmienne lokalne i globalne

#Precyzja liczby
x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7800
    iloscChf = value/kursChf
    iloscChf = "{0:.0f}".format(iloscChf)
    return iloscChf

chf = plnToChf(100)
print(chf)

##############

zmiennaGlobala = 10
print(f'\nZmienna globalna: {zmiennaGlobala}')
print(f'\nId zmiennej globalnej: {id(zmiennaGlobala)}')

def spr():
    zmiennaGlobal = 20
    print(f'\nZmienna globalna wewnątrz funkcji: {zmiennaGlobala}')
    print(f'\nId zmiennej globalnej wewnątrz funkcji: {id(zmiennaGlobala)}')

spr()
print(f'\nZmienna globalna po wyjściu z funkcji: {zmiennaGlobala}')
