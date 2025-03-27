#DIA 9
print('NIVEL 1')

#Ejercicio 1
print('Ejericio 1')
edad = int(input('Introduzca su edad: '))
if edad >= 18:
    print('Tiene la edad suficiente para conducir')
else:
    añosf = 18 - edad
    print(f'Faltan {añosf} años para que puedas concucir')

#Ejercicio 2
print('Ejericio 2')
my_age = int(input('Ingrese su edad: '))
your_age = int(input('Ingrese la edad de la otra persona: '))
if my_age > your_age:
    d = my_age - your_age
    if d == 1:
        print(f'Yo soy mayor que tú por {d} año.')
    else:
        print(f'Yo soy mayor que tú por {d} años.')
elif my_age < your_age:
    di = your_age - my_age
    if di == 1:
        print(f'Tú eres mayor que yo por {di} año.')
    else:
        print(f'Tú eres mayor que yo por {di} años.')
else:
    print('Tenemos la misma edad.')

#Ejercicio 3
print('Ejericio 3')
a = int(input('Escriba el primer numero (a): '))
b = int(input('Escriba el segundo numero (b): '))
if a > b:
    print(f'{a} es mayor a {b}')
elif a < b:
    print(f'{b} es mayor a {a}')
else:
    print(f'{a} y {b} son iguales')

print('NIVEL 2')

#Ejercicio 1
print('Ejericio 1')
calificaciones = int(input('Escriba su calificacion del 0 al 100: '))
if 80 <= calificaciones <= 100:
    print('A')
elif 70 <= calificaciones <= 79:
    print('B')
elif 60 <= calificaciones <= 69:
    print('C')
elif 50 <= calificaciones <= 59:
    print('D')
elif 0 <= calificaciones <= 49:
    print('F')
else:
    print('Puntuacion fuera del rango permitido')

#Ejercicio 2
print('Ejericio 2')
mes = input('Ingrese el mes en minusculas: ').lower()
if mes in ['septiembre', 'octubre', 'noviembre']:
   print('La estacion del año es otoño')
elif mes in ['diciembre', 'enero', 'febrero']:
   print('La estacion del año es invierno')
elif mes in ['marzo', 'abril', 'mayo']:
   print('La estacion del año es primavera')
elif mes in ['junio', 'julio', 'agosto']:
   print('La estacion del año es verano')
else:
   print('Mes no valido')

#Ejercicio 3
print('Ejericio 3')
fruits = ['banana', 'orange', 'mango', 'lemon']
f = input('Escribe el nombre de una fruta: ').lower()
if f in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(f)
    print('La fruta ya se añadio con exito. Esta es la lista actualizada: ', fruits)

print('NIVEL 3')

person = {
    'first_name': 'Luis',
    'last_name': 'Sanchez',
    'age': 20,
    'country': 'Mexico',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Rep. de Peru',
        'zipcode': '219'
    }
    }

#Ejercicio 1
print('Ejericio 1')
if 'skills' in person:
 lhabilidades = person['skills']
 imedio = len(lhabilidades) // 2
 print('La habilidad del medio es: ', lhabilidades[imedio])

#Ejercicio '
print('Ejericio 2')
if 'skills' in person and 'Python' in person['skills']:
    print('La persona tiene la habilidad de Python: ', True)
else:
    print('La persona tiene la habilidad de Python: ', False)

#Ejercicio 3
print('Ejericio 3')
if 'skills' in person:
    habilidades = set(person['skills'])  
if habilidades == {'JavaScript', 'React'}:
        print('Es un desarrollador front-end')
elif habilidades >= {'Node', 'Python', 'MongoDB'}:
        print('Es un desarrollador back-end')
elif habilidades >= {'React', 'Node', 'MongoDB'}:
        print('Es un desarrollador fullstack')
else:
        print('Esa habilidad no esta')

#Ejercicio 4
print('Ejericio 4')
if person.get('is_marred') == True and person.get('country') == 'Mexico':
    print(f'{person['first_name']} {person['last_name']} vive en {person['country']}. El esta casado.')