#DIA 8

#Ejercicio 1
print('Ejericio 1')
perro = {}

#Ejercicio 2
print('Ejericio 2')
perro = {
    'Nombre': 'Vitto',
    'Color' : 'Cafe',
    'Raza' : 'Chihuahua',
    'Patas' : 'Cuatro',
    'Edad' : 'Cinco años',        
         }

#Ejercicio 3
print('Ejericio 3')
estudiante = {
    'first_name' : 'Luis',
    'last_name' : 'Sanchez',
    'Sexo' : 'Masculino',
    'Edad' : 20,
    'Estado_civil' : 'Soltero',
    'Habilidades' : ['Python', 'Java', 'Análisis de Datos'],
    'País' : 'México',
    'Ciudad' : 'Calvillo',
    'Dirección' : 'Calle 123, Colonia Centro'
}

#Ejercicio 4
print('Ejericio 4')
print('La longitud del diccionario estidiante es: ', len(estudiante))

#Ejercicio 5
print('Ejericio 5')
habilidades = estudiante['Habilidades']
print('Las habilidades son: ', habilidades)
print('El tipo de dato es: ', type(habilidades))

#Ejercicio 6
print('Ejericio 6')
estudiante['Habilidades'].append('SQL')
estudiante['Habilidades'].append('C++')
print('El diccionario de habilidades actualizadas: ', estudiante['Habilidades'])

#Ejercicio 7
print('Ejericio 7')
claves = list(estudiante.keys())
print('Las claves del diccionario es: ', claves)

#Ejercicio 8
print('Ejericio 8')
valores = list(estudiante.values())
print('Los valores del diccionario son: ', valores)

#Ejercicio 9
print('Ejericio 9')
tuplas = list(estudiante.items())
print('La lista en forma de tuplas: ', tuplas)

#Ejercicio 10
print('Ejericio 10')
del estudiante['País']
print(estudiante)

#Ejercicio 11
print('Ejericio 11')
del estudiante
