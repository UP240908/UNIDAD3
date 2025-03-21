#DIA 5
print('NIVEL 1')

#Ejercicio 1
print('Ejericio 1')
lista = []

#Ejercicio 2
print('Ejericio 2')
lista = [1, 2, 3, 4, 5, 6]

#Ejercicio 3
print('Ejericio 3')
print(len(lista))

#Ejercicio 4
print('Ejericio 4')
pri = lista[0]
med = lista[len(lista)//2]
ult = lista[-1]
print(pri, med, ult)

#Ejercicio 5
print('Ejericio 5')
mixed_data_types = ['Luis Angel Sanchez Ponce', 20, 1.82, 'Soltero', '119 Rep.Peru']

#Ejercicio 6
print('Ejericio 6')
it_companies = ['Facebook' ,'Google' ,'Microsoft' ,'Apple' ,'IBM' ,'Oracle' ,'Amazon']

#Ejercicio 7
print('Ejericio 7')
print(it_companies)

#Ejercicio 8
print('Ejericio 8')
print(len(it_companies))

#Ejercicio 9
print('Ejericio 9')
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

#Ejercicio 10
print('Ejericio 10')
it_companies[5] = 'Tik Tok'
print(it_companies)

#Ejercicio 11
print('Ejericio 11')
it_companies.append('Instagram')
print(it_companies)

#Ejercicio 12
print('Ejercicio 12')
it_companies.insert(len(it_companies)//2, 'Whats App')
print(it_companies)

#Ejericio 13
print('Ejericio 13')
it_companies[3]= it_companies[3].upper()
print(it_companies)

#Ejericio 14
print('Ejericio 14')
print('#; '.join(it_companies))

#Ejericio 15
print('Ejericio 15')
print('Microsoft' in it_companies)

#Ejercicio 16
print('Ejericio 16')
it_companies.sort()
print(it_companies)

#Ejercicio 17
print('Ejericio 17')
it_companies.reverse()
print(it_companies)

#Ejercicio 18
print('Ejericio 18')
print(it_companies[:3])

#Ejercicio 19
print('Ejericio 19')
print(it_companies[-3:])

#Ejercicio 20
print('Ejercicio 20')
m = len(it_companies) //2
print(it_companies[:m] + [it_companies[m+1:]])

#Ejercicio 21
print('Ejercicio 21')
it_companies.pop(0)
print(it_companies)

#Ejercicio 22
print('Ejercicio 22')
m = len(it_companies) //2
del it_companies[m]
print(it_companies)

#Ejercicio 23
print('Ejercicio 23')
it_companies.pop()
print(it_companies)

#Ejercicio 24
print('Ejercicio 24')
it_companies.clear()
print(it_companies)

#Ejercicio 25
print('Ejercicio 25')
del it_companies

#Ejercicio 26
print('Ejercicio 26')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#Ejercicio 27
print('Ejercicio 27')
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

#NIVEL 2
print('NIVEL 2')

#Ejercicio 1
print('Ejericio 1')
años = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ejercicio 1.1
print('Ejericio 1.1')
años.sort()
min_edad = min(años)
max_edad = max(años)
print('Edades ordenadas: ', años)
print('Edad mas pequeña: ', min_edad, 'Edad mas grande: ', max_edad)

#Ejercicio 1.2
print('Ejericio 1.2')
años.append(min_edad)
años.append(max_edad)
print('Tabla actualizada: ', años)

#Ejercicio 1.3
print('Ejericio 1.3')
año = len(años)
if año % 2 == 0:
    media_años = (años[año//2 - 1] + años[año//2] / 2)
else:
    media_años = años[año//2]
print('La edad media es: ', media_años)

#Ejercicio 1.4
print('Ejericio 1.4')
prom = sum(años) / len(años)
print('La edad promedio es: ', prom)

#Ejercicio 1.5
print('Ejericio 1.5')
rango = max_edad - min_edad
print('El rango de edades es: ', rango)

#Ejercicio 1.6
print('Ejericio 1.6')
min_prom = abs(min_edad - prom)
max_prom = abs(max_edad - prom)
print('El min - promedio es: ',min_prom,'\n' 'El max - promedio es: ', max_prom)

#Ejercicio 2
print('Ejericio 2')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

countries.sort()
country  = len(countries)
if country % 2 == 0:
    med = countries[country//2 - 1:country//2 + 1]
else:
    med = countries[country//2]
print('El pais (es) del medio son: ', med)

#Ejercicio 3
print('Ejericio 3')
uno = countries[:(country+1)//2]
dos = countries[(country+1)//2:]
print('La primera lista es: ', uno)
print('La segunda lista es: ', dos)

#Ejercicio 4
print('Ejericio 4')
tabla = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
first, second, third, * tres = tabla
print('Primeros tres paises: ', first ,  second,  third)
print('Paises escandinavos: ', tres)