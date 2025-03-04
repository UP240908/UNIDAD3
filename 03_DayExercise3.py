import math

#Ejercicio 1
Edad = 19
Edad = int
#Ejercicio 2
Altura = 1.80
Altura = float

#Ejercicio 3
Complejo = 1j

#Area del tringulo
base = float(input('Ingresa la base del traingulo '))
altura = float(input('Ingresa la altura del triangulo '))
area =base*altura/2
print('El area es de: ' ,area)

#Perimetro del triangulo
lado1 = float(input('Ingresa la longitud de un lado '))
lado2 = float(input('Ingresa el segundo lado '))
lado3 = float(input('Ingresa el tercer lado '))
perimetro = lado1+lado2+lado3
print('El perimetro del triangulo es de: ' , perimetro)

#Area y perimetro del rectangulo
l1 = float(input('Ingrese la altura del rectangulo '))
l2 = float(input('Ingrese la base del rectangulo '))
Area = l1*l2
Perimetro = 2*(l1+l2)
print('El area del rectangulo es de: ' , Area)
print('El perimetro del rectangulo es de: ' , Perimetro)

#Circulo
Radio =float(input('Ingrese el radio del circulo '))
Pi = 3.1416
Area = Pi*(Radio*Radio)
Circunferencia = 2*Pi*Radio
print('El area del cirulo es de: ' , Area)
print('La circunferencia del circulo es de: ' , Circunferencia)

#PENDIENTE DE V 1
#z = 2q-2   q = x z =y
q1, z1, q2, z2 = 1, 0, 0, -2
primerapendiente = (z2 - z1)/(q2-q1)
print('La pendiente es: ' , primerapendiente)

#PENDIENTE DE V 2
x1, y1, x2, y2 = 2, 2, 6, 10
Segundapendiente= (y2-y1)/(x2-x1)
print('La pendiente es: ' , Segundapendiente)
euclideandistancia = math.sqrt((x2-x1) **2 + (y2-y1) **2)
print('La distancia Eucladiana es: ' , euclideandistancia)

#Ejercicio 10
if (primerapendiente == Segundapendiente):
    print('Es lo mismo')
else: print('No es lo mismo estas equivocado!')

#Ejercicio 11 
a = int(input('Ingrese el valor de x'))
b = int(x*2+ 6* + 9)
print=('El valor de x es: ' , b)

#Ejercicio 12
palabra1 = len('Python')
palabra2 = len('Dragon')
if (palabra1 != palabra2):
    print('Tienen diferente longitud')
else : 'Tienen la misma longitud'

#Ejercicio 13
print('on'in 'P2ython'and 'on'in 'Dragon')

#Ejercicio 14
print('Jerga' in 'Espero que este curso no esté lleno de jerga.')

#Ejercicio 15
print('no' in 'Dragon' and 'no' in 'Python')

#Ejercicio 16
pythonlen = len('Python')
print(float(pythonlen))
print(int(pythonlen))

#Ejercicio 17
num= int(input())
if num %2:
    print('El numero es par')
else: print('El nuimero no es par')

#Ejercicio 18
d = 7//8
r= 2.7
if d==r:
    print('Si es igual')
else: print('No es igual')

#Ejercicio 19
comparar = type(10)
if comparar== 10:
    print('Si es igual a 10')
else: print('No es igual a 10')

#Ejercicio 20
va =int(9.8)
if va == 10:
    print('El valor de 9.8 sin es igual a 10')
else: print('El valor de 9.8 no es igual a 10')

#Ejercicio 21
horas= int(input('Ingrese sus horas laborales'))
pago = int(input('Ingrese su sueldo por hora'))
sueldot=horas*pago
print('Su sueldo es de: ', sueldot)

#Ejercicio 22
años=int(input('Ingrese sus años vividos'))
t= años*3600*24*365
print('El total de segundos vividos es de: ', t)

#Ejercicio 23
for i in range(1,6):
    print(i, 1, i**2,i**2, i**3)
