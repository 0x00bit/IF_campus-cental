import math

x = float(input('Insira o lado(x) do triângulo: '))
y = float(input('Insira o lado(y) do triângulo: '))
z = float(input('Insira o lado(z) do triângulo: '))

if x + y < z or x + z < y or y + z < x:
    print ('Valores inválidos para um triângulo')
    quit()

ang_1 = math.degrees(math.acos((y**2 + z**2 - x**2)/(2*y*z)))
ang_2 = math.degrees(math.acos((x**2 + z**2 - y**2)/(2*x*z)))
ang_3 = 180 - ang_1 - ang_2

print('Lados do triâgulo: ')
print(f'{round(ang_1, 2)}°')
print(f'{round(ang_2, 2)}°')
print(f'{round(ang_3, 2)}°')
print(40*'=')

if x == y and y == z:
    print('Triângulo Equilatero,')
elif x == y or y == z or x == z:
    print('Triângulo Isósceles,')
else:
    print('Triângulo Escaleno,')

if ang_1 > 90 or ang_2 > 90 or ang_3 > 90:
    print('Ângulo obtuso.')
elif ang_1 == 90 or ang_2 == 90 or ang_3 == 90:
    print('Ângulo retângular.')
else:
    print('Ângulo agudo.')
