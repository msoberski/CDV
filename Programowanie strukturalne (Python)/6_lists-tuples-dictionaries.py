#Listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')

#Tuple
names = ('Anna', 'Janusz')
print(type(names))

names2 = ('Anna')
print(type(names2))

first = names[0]
print(first)

#Słowniki
person = {
    'name':'Janusz',
    'city':'Poznań',
    'job':'director',
    'age':30,
    'children':True
    }

print(type(person))
print(person)
print(person['city'])

print(person.get('job', 'brak klucza'))
