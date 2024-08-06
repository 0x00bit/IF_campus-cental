import sys

n = int(input('> '))
count = 0

if n <= 0:
    sys.exit('Informe um numero valido')

while n > 0:
    n //= 10
    count += 1

print(f"O Numero possui: {count} digitos")

