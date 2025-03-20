#DIA 4
#Ejercicio 1
print('Ejericio 1')
p1 = 'Thirty'
p2 = 'Days'
p3 = 'Of'
p4 = 'Python'
e = ' '
concatenar = p1+e+p2+e+p3+p4
print(concatenar)

#Ejercicio 2
print('Ejericio 2')
p1 = 'Coding'
p2 = 'For'
p3 = 'All'
e = ' '
concatenar = p1+e+p2+e+p3
print(concatenar)

#Ejercicio 3
print('Ejericio 3')
company= 'Coding For All'

#Ejercicio 4
print('Ejericio 4')
print(company)

#Ejercicio 5
print('Ejericio 4')
print(len(company))

#Ejercicio 6
print('Ejericio 6')
print(company.upper())

#Ejercicio 7
print('Ejericio 7')
print(company.lower())

#Ejercicio 8
print('Ejericio 8')
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Ejercicio 9
print('Ejericio 9')
a1 = company.replace('Coding','')
print(a1)

#Ejercicio 10
print('Ejericio 10')
print(company.index('Coding'))
print(company.find('Coding'))

#Ejercicio 11
print('Ejericio 11')
print(company.replace('Coding','Python'))

#Ejercicio 12
print('Ejericio 12')
company2 = 'Python For Everyone'
print(company2.replace('Everyone','All'))

#Ejericio 13
print('Ejericio 13')
print(company.split(' '))

#Ejericio 14
print('Ejericio 14')
t1 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(t1.split(','))

#Ejericio 15
print('Ejericio 15')
print(company[0])

#Ejercicio 16
print('Ejericio 16')
print(company.rindex('l'))

#Ejercicio 17
print('Ejericio 17')
print(company[10])

#Ejercicio 18
print('Ejericio 18')
pri = company2.index('P')
sec = company2.index('F')
ter = company2.index('E')
print(company2[pri]+company2[sec]+company2[ter])

#Ejercicio 19
print('Ejericio 19')
pri = company.index('C')
sec = company.index('F')
ter = company.index('A')
print(company[pri]+company[sec]+company[ter])

#Ejercicio 20
print('Ejericio 20')
print(company.index('C'))

#Ejercicio 21
print('Ejericio 21')
print(company.index('F'))

#Ejercicio 22
print('Ejericio 22')
t1 = 'Coding For All People'
print(t1.rfind('l'))

#Ejercicio 23
print('Ejericio 23')
t1 = 'You cannot end a sentence with because because because is a conjunction'
print(t1.find('because'))

#Ejercicio 24
print('Ejericio 24')
print(t1.rindex('because'))

#Ejercicio 25
print('Ejericio 25')
print(t1[0:30]+t1[54:75])

#Ejercicio 26
print('Ejericio 26')
print(t1.index('because'))

#Ejercicio 27
print('Ejericio 27')
print(t1[0:30]+t1[54:75])

#Ejercicio 28
print('Ejericio 28')
print(company.startswith('Coding'))

#Ejercicio 29
print('Ejericio 29')
print(company.endswith('coding'))

#Ejericico 30
print('Ejericio 30')
print(company.replace(' ' , ''))

#Ejercicio 31
print('Ejericio 31')
t1 = '30DaysOfPython'
t2 = 'thirty_days_of_python'
if t1.isidentifier()==False:
    print('30DaysOfPython :No es un identificador valido')
else: t2.isidentifier()==True
print('thirty_days_of_python :Es un identificador valido')
 
#Ejercicio 32
print('Ejericio 32')
pyli = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon' 
print(pyli.__hash__())

#Ejercicio 33
print('Ejericio 33')
print('I am enjoying this challenge.\nI just wonder what is next.'  )

#Ejercicio 34
print('Ejericio 34')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki') 

#Ejercicio 35
print('Ejericio 35')
radio = 10
area = 3.14 * radio ** 2
output = "The area of a circle with radius {} is {} meters square.".format(radio, area)
print(output)

#Ejercicio 36
print('Ejericio 36')
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))