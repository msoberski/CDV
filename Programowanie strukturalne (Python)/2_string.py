tekst = "Anna, paweł, julIA"

lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
print(imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
print("\nPodaj swoje nawisko: ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)

tekst1 = "\nJulia\n"
tekst2 = "Nowak"
print(tekst1 + tekst2)

tekst1 = tekst1.rstrip()
print(tekst1 + " " + tekst2)

#wszystkie wersje Pythona
tekst = "%s, Java i %s" % ("PHP", "Python")
print(tekst)

#nowsze wersje Pythona (od 2.6 w górę)
tekst = "{1}, Java i {0}".format("PHP", "Python")
print(tekst)

#help(text.replace)
nowy = tekst.replace("PHP", "C#")
print(nowy)

#wypisanie danych
rok = 2019
miesiac = "kwiecien"
dzien = 27
print("\nData: ",end="")
print(dzien,miesiac,rok,sep="-")
