#DIA 10
print('NIVEL 1')

#Ejercicio 1
print('Ejericio 1')
print('Bucle While')
count = 0
while count <= 10:  
    print(count)
    count += 1  

print('Bucle For')
for count in range (11):
 print(count)

#Ejercicio 2
print('Ejericio 2')
print('Bucle While')
count = 0
con = 10 
while con >= 0:  
    print(con)
    con -= 1  

print('Bucle For')
for con in range(10, -1, -1):  
 print(con)

#Ejercicio 3
print('Ejericio 3')
e3 = 1  
while e3 <= 7:  
 print('#' * e3)  
 e3 += 1 
 
#Ejercicio 4
print('Ejericio 4')
e2 = 0  
while e2 < 8: 
    j2 = 0  
    while j2 < 8:  
        print('#', end=' ') 
        j2 += 1  
    print()  
    e2 += 1  
 

#Ejercicio 5
print('Ejericio 5')
e4 = 0  
while e4 <= 10:  
 print(f'{e4} x {e4} = {e4 * e4 }')  
 e4 += 1  

#Ejercicio 6
print('Ejericio 6')
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lista in lista: 
 print(lista)

#Ejercicio 7
print('Ejericio 7')
for e7 in range(101):  
    if e7 % 2 == 0:  
     print(e7)

#Ejercicio 8
print('Ejericio 8')
for e8 in range(101):  
    if e8 % 2 != 0:  
     print(e8)

print('NIVEL 2')

#Ejercicio 1
print('Ejericio 1')
suma = 0  
for i in range(101):  
 suma += i  
print('La suma de todos los numeros es: ', suma)  

#Ejercicio 1.1
print('Ejericio 1.1')
sumap = 0 
sumai = 0  
for i in range(101):  
    if i % 2 == 0:  
        sumap += i  
    else:  
        sumai += i  
print(f'La suma de todos los pares es: {sumap}')  
print(f'Y la suma de todos los impares es: {sumai}')  

print('NIVEL 3')

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

#Ejercicio 1
print('Ejericio 1')
paises_con_tierra = [pais for pais in countries if 'tierra' in pais.lower()]
print('Países que contienen la palabra tierra: ')
for pais in paises_con_tierra:
    print(pais)

#Ejercicio 2
print('Ejericio 2')
f = ['plátano', 'naranja', 'mango', 'limón']
frutasi = []
for f in reversed(f):
    frutasi.append(f)
print(frutasi)

#Ejercicio 3.1
print('Ejericio 3.1')
from countries_data.py import countries
idiomas = set()
for pais in countries:
    idiomas.update(pais['languages']) 
print(f'El número total de idiomas es: {len(idiomas)}')

#Ejercicio 3.2
print('Ejericio 3.2')
from collections import Counter
idiomas = Counter()
for pais in countries:
    for idioma in pais['languages']:
        idiomas[idioma] += 1
top = idiomas.most_common(10)
print('Los 10 idiomas más hablados son:' )
for idioma, cantidad in top:
    print(f'{idioma}: {cantidad} países')

#Ejercicio 3.3
print('Ejericio 3.3')
top = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]
print('Los 10 países más poblados son: ')
for pais in top:
    print(f"{pais['country']}: {pais['population']} personas")