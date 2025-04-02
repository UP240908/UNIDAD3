#DIA 11
print('NIVEL 1')

#Ejercicio 1
print('Ejericio 1')
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())

#Ejercicio 2
print('Ejericio 2')
import random
import string

def user_id_gen_by_user():
    caracteres = int(input('Ingrese el número de caracteres por IDs: '))
    IDs = int(input('Ingrese la cantidad de IDs a generar: '))

    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=caracteres)) for _ in range(IDs)]
    return ids

print(user_id_gen_by_user())

#Ejercicio 3
print('Ejericio 3')
import random

def rgb_color_gen():
    uno = random.randint(0, 255)
    dos = random.randint(0, 255)
    tres = random.randint(0, 255)
    return f'rgb({uno},{dos},{tres})'

print(rgb_color_gen())
print(rgb_color_gen())

print('NIVEL 2')

#Ejercicio 1
print('Ejericio 1')
import random

def list_of_hexa_colors(e1):
    colores = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(e1)]
    return colores

print(list_of_hexa_colors(5)) 

#Ejercicio 2
print('Ejericio 2')
import random

def list_of_rgb_colors(e2):
    eje2 = [f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})' for _ in range(e2)]
    return eje2

print(list_of_rgb_colors(5))  

#Ejercicio 3
print('Ejericio 3')
import random

def generate_colors(color, e3):
    if color == 'hexa':
        return ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(e3)]
    elif color == 'rgb':
        return [f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})' for _ in range(e3)]
    else:
        return "Tipo de color no válido. Usa 'hexa' o 'rgb'"

print(generate_colors('hexa', 3))  
print(generate_colors('rgb', 1))   

print('NIVEL 3')

#Ejercicio 1
print('Ejericio 1')
import random

def shuffle_list(e11):
    progra = e11[:]  
    random.shuffle(progra)
    return progra

numeros = [1, 2, 3, 4, 5]
print(shuffle_list(numeros)) 

#Ejercicio 2
print('Ejericio 2')
import random

def numeros_randoms():
    return random.sample(range(10), 7)

print(numeros_randoms())  