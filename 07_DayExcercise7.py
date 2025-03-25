#DIA 7
print('NIVEL 1')

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicio 1
print('Ejericio 1')
print(len(it_companies))

#Ejercicio 2
print('Ejericio 2')
it_companies.add('Twitter')
print(it_companies)

#Ejercicio 3
print('Ejericio 3')
it_companies.update(['Tik tok', 'Mercado libre', 'Instagram'])
print(it_companies)

#Ejercicio 4
print('Ejericio 4')
it_companies.remove('Mercado libre')
print(it_companies)

#Ejercicio 5
print('Ejericio 5')
it_companies.discard('Chat GPT')
print(it_companies)

print('NIVEL 2')

#Ejercicio 1    
print('Ejericio 1')
c = B.union(A)
print(c)

#Ejercicio 2   
print('Ejericio 2')
print(A.intersection(B))

#Ejercicio 3
print('Ejericio 3')
print(A.issubset(B))

#Ejercicio 4
print('Ejericio 4')
print(A.isdisjoint(B))

#Ejercicio 5    
print('Ejericio 5')
print(A.union(B))
print(B.union(A))

#Ejercicio 6
print('Ejericio 6')
print(A.symmetric_difference(B))

#Ejercicio 7    
print('Ejericio 7')
del A
del B

print('NIVEL 3')

#Ejercicio 1   
print('Ejericio 1')
mmm = set(age)
print ('El conjunto es: ', len(mmm))
print('La lista es: ', len(age))

#Ejercicio 2   
print('Ejericio 2')
#Una cadena es una secuencia de caracteres usada para representar texto. Se escribe entre comillas ("" o '').
#Una lista es una colección ordenada de elementos, que pueden ser de cualquier tipo (números, cadenas, otras listas, etc.).
#Una tupla es similar a una lista, pero no se puede modificar después de su creación. Se usa cuando no queremos que los datos cambien.Una vez creada no se puede modificar
#Un conjunto es una colección desordenada de elementos únicos (no permite duplicados).

#Ejercicio 3    
print('Ejericio 3')
pal = 'I am a teacher and I love to inspire and teach people'
w = set (pal.split())
print(len(w))