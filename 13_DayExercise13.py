#DIA 13

#Ejercicio 1
print('Ejericio 1')
lista = [-4, -3, -2, -1, 0, 2, 4, 6]

filtrados = [num for num in lista if num <= 0]

print(filtrados) 

#Ejercicio 2
print('Ejericio 2')
listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list = [item for sublist1 in listas for sublist2 in sublist1 for item in sublist2]

print(list)  

#Ejercicio 3
print('Ejericio 3')
lista_en_tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(lista_en_tuplas)

#Ejercicio 4
print('Ejericio 4')
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

pais = [
    [country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in paises for country in sublist]

print(pais)

#Ejercicio 5
print('Ejericio 5')
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

diccionarios = [
    {'country': paises[0].upper(), 'city': paises[1].upper()} 
    for sublist in paises 
    for paises in sublist
]

print(diccionarios)

#Ejercicio 6
print('Ejericio 6')
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenar= [f"{name[0][0]} {name[0][1]}" for name in nombres]

print(concatenar)

#Ejercicio 7
print('Ejericio 7')
a = lambda m, b: (m, b)
s, i = a(3, 5)
print(f'Pendiente: {s}, Intersección con el eje y: {i}')