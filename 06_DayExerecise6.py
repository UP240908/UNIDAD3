#DIA 6
print('NIVEL 1')

#Ejercicio 1
print('Ejericio 1')
tuple = ()

#Ejercicio 2
print('Ejericio 2')
hermanos = ('Juanjo', 'Aldo', 'Santiago')
hermanas = ('Maria',)

#Ejercicio 3
print('Ejericio 3')
unir = hermanos + hermanas
print('Todos mis hermanos: ', unir)

#Ejercicio 4
print('Ejericio 4')
print('Numero de hermanos: ', len(unir))

#Ejercicio 5
print('Ejericio 5')
family_members = unir + ('Juan Jose', 'Maria Elena')
print('La familia completa es: ', family_members)

#Nivel 2
print('NIVEL 2')

#Ejercicio 1
print('Ejericio 1')
*unir, Juan_jose, Maria_Elena = family_members
print('Hermanos: ', unir)
print('Papas: ', Juan_jose, Maria_Elena)

#Ejercicio 2
print('Ejericio 2')
frutas = ('Fresa', 'Guayaba', 'Sandia')
verduras = ('Zanahoria', 'Lechuga', 'Tomate')
otros = ('Huevos', 'Atun', 'Leche')
food_stuff_tp = frutas + verduras + otros 

#Ejercicio 3
print('Ejericio 3')
food_stuff_lt = list(food_stuff_tp)
print('Lista de comida: ', food_stuff_lt)

#Ejercicio 4
print('Ejericio 4')
lol = len(food_stuff_lt)
mitad = food_stuff_lt[(lol-1)//2 : lol//2 + 1]
print('Comida del medio: ', mitad)

#Ejercicio 5
print('Ejericio 5')
print('Primeras tres comidas: ', food_stuff_lt[:3])
print('Ultimas tres comidas tres comidas: ', food_stuff_lt[-3:])

#Ejercicio 6
print('Ejericio 6')
del food_stuff_tp

#Ejercicio 7
print('Ejericio 7')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia es un pais nordico: ', 'Estonia' in nordic_countries)
print('Islandia es un pais nordico: ', 'Iceland' in nordic_countries)