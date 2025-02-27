import math

#Ejercicio 1
Edad = 19

#Ejercicio 2
Altura = 1.80

#Ejercicio 3
Complejo = 1j

#Area del tringulo
base = float(input('Ingresa la base del traingulo'))
altura = float(input('Ingresa la altura del triangulo'))
area = float(input(0.5*base*altura))
print('El area es de: ' , area)

#Perimetro del triangulo
lado1 = float(input('Ingresa la longitud de un lado'))
lado2 = float(input('Ingresa el segundo lado'))
lado3 = float(input('Ingresa el tercer lado'))
perimetro = lado1+lado2+lado3
print('El perimetro del triangulo es de: ' , perimetro)

#Area y perimetro del rectangulo
l1 = float(input('Ingrese la altura del rectangulo'))
l2 = float(input('Ingrese la base del rectangulo'))
Area = l1*l2
Perimetro = 2*(l1+l2)
print('El area del rectangulo es de: ' , Area)
print('El perimetro del rectangulo es de: ' , Perimetro)

#Circulo
Radio =float(input('Ingrese el radio del circulo'))
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
